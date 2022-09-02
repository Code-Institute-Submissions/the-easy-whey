# Generated by Django 3.2 on 2022-09-02 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('subscription', '0014_alter_subscription_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='user_profile',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptions', to='profiles.userprofile'),
        ),
    ]
