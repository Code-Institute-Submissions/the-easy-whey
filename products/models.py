from django.db import models

# Create your models here.
class Product(models.Model):
    """
    Model for the individual protein powder
    """
    flavour = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, default="6.99")

    def __str__(self):
        return self.flavour


class Nutrition(models.Model):
    """
    Model for the nutritional content of products
    """
    class Meta:
        verbose_name_plural = "Nutrition"

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
    """
    Model for ingredients for each product
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ingredient')
    name = models.CharField(max_length=50, blank=False, null=False, default="You need an ingredient")
 
    def __str__(self):
        return f"ingredient - {self.product} ingredients"
