from django.contrib import admin
from .models import Product, Nutrition, Ingredient

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('flavour', 'description', 'size', 'price') 


class NutritionAdmin(admin.ModelAdmin):
    list_display = ('product','energy', 'fat', 'carbohydrate', 'sugars', 'protein', 'salt')


admin.site.register(Product, ProductAdmin)
admin.site.register(Nutrition, NutritionAdmin)
admin.site.register(Ingredient)
