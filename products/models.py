from django.db import models

# Create your models here.
class Product(models.Model):
    flavour = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, default="12.99")

    def __str__(self):
        return self.flavour


class Nutrition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='nutrition')
    energy = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    sugars = models.FloatField()
    protein = models.FloatField()
    salt = models.FloatField()

    def __str__(self):
        return f"{self.product} nutrition"


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ingredient')
    ingredient_one = models.CharField(max_length=35, blank=False, null=False, default="You need an ingredient")
    ingredient_two = models.CharField(max_length=35, blank=True, null=False)
    ingredient_three = models.CharField(max_length=35, blank=True, null=False)
    ingredient_four = models.CharField(max_length=35, blank=True, null=False)
    ingredient_five = models.CharField(max_length=35, blank=True, null=False)
    ingredient_six = models.CharField(max_length=35, blank=True, null=False)
    ingredient_seven = models.CharField(max_length=35, blank=True, null=False)
    ingredient_eight = models.CharField(max_length=35, blank=True, null=False)
    ingredient_nine = models.CharField(max_length=35, blank=True, null=False)
    ingredient_ten = models.CharField(max_length=35, blank=True, null=False)

    def __str__(self):
        return f"ingredient - {self.product} ingredients"
