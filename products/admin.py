from django.contrib import admin
from .models import Product, Nutrition, Ingredient

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", 'flavour', 'description', 'price', "image_url", "image")


class NutritionAdmin(admin.ModelAdmin):
    list_display = ('product','energy', 'fat', 'carbohydrate', 'sugars', 'protein', 'salt')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('product', 'name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Nutrition, NutritionAdmin)
admin.site.register(Ingredient, IngredientAdmin)
