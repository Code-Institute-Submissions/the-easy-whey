from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from easy_whey.validators import phone_regex

# Create your models here.


class UserProfile(models.Model):
    """
    Models a user profile
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_address_one = models.CharField(
        max_length=100, null=True, blank=True
    )
    default_address_two = models.CharField(
        max_length=100, null=True, blank=True
    )
    default_town_city = models.CharField(max_length=50, null=True, blank=True)
    default_postcode = models.CharField(max_length=50, null=True, blank=True)
    default_phone_number = models.CharField(
        validators=[phone_regex], max_length=11, null=True, blank=True
    )
    default_county = models.CharField(max_length=50, null=True, blank=True)
    default_country = CountryField(
        blank_label="Country", null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.user}"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    function to create or update a user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
