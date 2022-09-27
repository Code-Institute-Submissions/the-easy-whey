import uuid
from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile
from easy_whey.validators import phone_regex


class Order(models.Model):
    """
    Models an order
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(
        validators=[phone_regex], max_length=11, null=True, blank=True
    )
    address_one = models.CharField(max_length=100, null=False, blank=False)
    address_two = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=50, null=True, blank=True)
    town_city = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=50, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False, default=0
    )
    is_paid = models.BooleanField(default=False)

    def _create_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.total_cost = self.lineitems.aggregate(Sum("product_total"))[
            "product_total__sum"
        ]
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Models the line items that are attached to an order
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    product_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        self.product_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"Product: {self.product.flavour} order: {self.order.order_number}"
        )
