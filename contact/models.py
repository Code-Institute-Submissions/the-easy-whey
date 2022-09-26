from django.db import models
from easy_whey.validators import phone_regex

# Create your models here.

class Contact(models.Model):
    """
    Model for the contact form
    """
    class Meta:
        verbose_name_plural = "Contact"

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(validators=[phone_regex], max_length=11, null=True, blank=True)
    message = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return f"Message received from {self.name}, {self.email}"