from django.db import models

# Create your models here.
class Product(models.Model):
    flavour = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    BAG_SZIES = (
    ("1","1 kg"),
    ("2","2 kg"),
    ("3","3 kg"),
    ("4","4 kg"),
    ("5","5 kg"),
    )
    size = models.CharField(max_length=1, choices=BAG_SZIES, null=False, blank=False, default="1")
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, default="14.99")

    def __str__(self):
        return self.flavour


class Nutrition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    energy = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    sugars = models.FloatField()
    protein = models.FloatField()
    salt = models.FloatField()

    def __str__(self):
        return f"{self.product} nutrition"


class Ingredient(models.Model):
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return f"ingredient - {self.name}"
