from django.forms import ValidationError

def validation_phone(phone):
    if ' ' in phone:
        raise ValidationError('Номер не может содержать пробелы!!!')
    
    if not phone.startswith('+7'):
        raise ValidationError('Неверный формат номера')
    elif len(phone) != 12:
        raise ValidationError('Длина номера должен состоять из 12 цифр')
    else:
        for i in phone[1:]:
            if not i.isdigit():
                raise ValidationError(f'Номер не может включать "{i}"')