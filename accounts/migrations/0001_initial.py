# Generated by Django 5.0.1 on 2024-01-18 05:04

import accounts.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15, unique=True, validators=[accounts.utils.validation_phone])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]