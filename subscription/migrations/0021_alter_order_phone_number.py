# Generated by Django 3.2 on 2022-09-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0020_alter_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]
