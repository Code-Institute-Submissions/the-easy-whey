from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Product(models.Model):
    """
    Model for the individual protein powder
    """

    flavour = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, blank=False, default="6.99"
    )

    def __str__(self):
        return f"Flavour: {self.flavour}"


class Nutrition(models.Model):
    """
    Model for the nutritional content of products
    """

    class Meta:
        verbose_name_plural = "Nutrition"

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="nutrition"
    )
    energy = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(999.99)]
    )
    fat = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(20.00)]
    )
    carbohydrate = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(20.00)]
    )
    sugars = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(20.00)]
    )
    protein = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.00)]
    )
    salt = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.00)]
    )

    def __str__(self):
        return f"{self.product} nutrition"


class Ingredient(models.Model):
    """
    Model for ingredients for each product
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="ingredient"
    )
    name = models.CharField(
        max_length=50, blank=False, null=False,
        default="You need an ingredient"
    )

    def __str__(self):
        return f"ingredient - {self.product} ingredients"
