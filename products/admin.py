from django.contrib import admin
from .models import Product, Nutrition, Ingredient

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('flavour', 'description', 'price')


class NutritionAdmin(admin.ModelAdmin):
    list_display = ('product','energy', 'fat', 'carbohydrate', 'sugars', 'protein', 'salt')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('product', 'ingredient_one','ingredient_two', 'ingredient_three', 'ingredient_four', 'ingredient_five', 'ingredient_six', 'ingredient_seven', 'ingredient_eight', 'ingredient_nine', 'ingredient_ten')

admin.site.register(Product, ProductAdmin)
admin.site.register(Nutrition, NutritionAdmin)
admin.site.register(Ingredient, IngredientAdmin)
