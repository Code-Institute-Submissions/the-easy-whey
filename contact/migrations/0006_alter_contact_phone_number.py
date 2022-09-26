# Generated by Django 3.2 on 2022-09-26 10:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: 07xxxxxxxxx', regex='^(07)\\d{9}$')]),
        ),
    ]
