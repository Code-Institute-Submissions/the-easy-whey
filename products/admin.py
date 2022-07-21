from django.contrib import admin
from .models import Product, Nutrition, Ingredient

# Register your models here.
admin.site.register(Product)
admin.site.register(Nutrition)
admin.site.register(Ingredient)