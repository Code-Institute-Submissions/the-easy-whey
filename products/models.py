from django.db import models

# Create your models here.
class Product(models.Model):
    flavour = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, default="12.99")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='products')

    def __str__(self):
        return self.flavour


class Nutrition(models.Model):

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ingredient')
    name = models.CharField(max_length=50, blank=False, null=False, default="You need an ingredient")
 
    def __str__(self):
        return f"ingredient - {self.product} ingredients"
