from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=50, null=True, blank=False)
    town_city = models.CharField(max_length=50, null=False, blank=False)
    address_one = models.CharField(max_length=100, null=False, blank=False)
    address_two = models.CharField(max_length=100, null=False, blank=False)
    county = models.CharField(max_length=50, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)