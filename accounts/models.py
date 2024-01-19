from django.db import models, transaction
from .utils import validation_phone
#from django.forms import ValidationError
from django.core.exceptions import ValidationError

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, validators=[validation_phone], unique=True)
    email = models.EmailField(blank=True, null=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.first_name} {self.balance}'
    
    def debit(self, amount):
        self.balance -= amount
        self.save()

    def credit(self, amount):
        self.balance += amount
        self.save()

class Transaction(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='receiver')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            self.sender.debit(self.amount)
            self.receiver.credit(self.amount)
            super().save(*args, **kwargs)

    def clean(self):
        if self.sender == self.receiver:
            raise ValidationError('Нельзя осуществить перевод самому себе')
        if self.sender.balance < self.amount:
            raise ValidationError('Недостаточно средств для перевода!!!')
        if self.amount < 0:
            raise ValidationError('Сумма должна быть положительной!')

    def __str__(self):
        return f'{self.sender} -> {self.receiver} {self.amount}'

class TransactionByPhone(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sender_phone')
    receiver = models.CharField(max_length=15, validators=[validation_phone])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.receiver} {self.amount}'
    
    def clean(self):
        if self.sender.balance < self.amount:
            raise ValidationError('Недостаточно средств для перевода!!!')
        if self.amount < 0:
            raise ValidationError('Сумма должна быть положительной!')
        if not Customer.objects.filter(phone=self.receiver).exists():
            raise ValidationError('Неверный номер телефона!')
        if self.sender.phone == self.receiver:
            raise ValidationError('Нельзя осуществить перевод самому себе')
        
        
    def save(self, *args, **kwargs):
        receiver = Customer.objects.get(phone=self.receiver)
        self.sender.debit(self.amount)
        receiver.credit(self.amount)
        super().save(*args, **kwargs)



