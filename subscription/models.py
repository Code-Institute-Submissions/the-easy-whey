import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product


# Create your models here.
# need to know the date the subscription started, the amount of protein they've chosen, the flavour(s) they've chosen, the delivery address, the name and contact info, something that lets me know they've payed
# mould more to a checkout kinda model, a form where they pick flavour and sizes which gets put into the database and onto payment and sub starting

class Subscription(models.Model):
    subscription_number = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=50, null=True, blank=True)
    town_city = models.CharField(max_length=50, null=False, blank=False)
    address_one = models.CharField(max_length=100, null=False, blank=False)
    address_two = models.CharField(max_length=100, null=False, blank=False)
    county = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    subscription_start_date = models.DateTimeField(null=True, blank=True)
    subscription_end_date = models.DateTimeField(null=True, blank=True)

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
    order = models.ForeignKey(Subscription, on_delete=models.CASCADE, null=False, blank=False, related_name="lineitems")
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    product_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.product_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Product: {self.product.name} for the subscription: {self.order.subscription_number}"