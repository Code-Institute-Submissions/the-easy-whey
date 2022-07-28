from django.contrib import admin
from .models import Product, Nutrition, Ingredient, Size

# Register your models here.
admin.site.register(Product)
admin.site.register(Nutrition)
admin.site.register(Ingredient)
admin.site.register(Size)