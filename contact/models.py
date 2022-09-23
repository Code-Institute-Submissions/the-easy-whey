from django.db import models

# Create your models here.

class Contact(models.Model):
    """
    Model for the contact form
    """
    class Meta:
        verbose_name_plural = "Contact"

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=50, null=False, blank=False)
    message = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return f"Message received from {self.name}, {self.email}"