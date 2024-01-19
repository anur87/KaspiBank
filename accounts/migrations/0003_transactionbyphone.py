# Generated by Django 5.0.1 on 2024-01-18 06:39

import accounts.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionByPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=15, validators=[accounts.utils.validation_phone])),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_phone', to='accounts.customer')),
            ],
        ),
    ]
