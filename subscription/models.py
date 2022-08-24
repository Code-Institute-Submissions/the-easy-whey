import uuid
from django.db import models
from django.db.models import Sum

from django_countries.fields import CountryField

from products.models import Product


class Subscription(models.Model):
    subscription_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=50, null=False, blank=False)
    address_one = models.CharField(max_length=100, null=False, blank=False)
    address_two = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=50, null=True, blank=True)
    town_city = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=50, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    subscription_start_date = models.DateField(null=True, blank=True)
    subscription_end_date = models.DateField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    def _create_subscription_number(self):
        return uuid.uuid4().hex.upper()

    
    def update_total(self):
        self.total_cost = self.lineitems.aggregate(Sum("product_total"))["product_total__sum"]
        self.save()


    def save(self, *args, **kwargs):
        if not self.subscription_number:
            self.subscription_number = self._create_subscription_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subscription_number


class SubscriptionLineItem(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, null=False, blank=False, related_name="lineitems")
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    product_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.product_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Product: {self.product.flavour} for the subscription: {self.subscription.subscription_number}"