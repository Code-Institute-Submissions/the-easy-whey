from django.shortcuts import render
from .models import Product, Nutrition, Ingredient
from .forms import ProductForm, NutritionForm, IngredientForm
# Create your views here.


def index(request):
    """
    Returns the homepage
    """
    return render(request, "products/index.html")


def product_detail(request):
    """
    Returns the product details page
    """
    chocolate_nutrition = Nutrition.objects.get(product_id=1)
    banana_nutrition = Nutrition.objects.get(product_id=2)
    strawberry_nutrition = Nutrition.objects.get(product_id=3)
    cookies_and_cream_nutrition = Nutrition.objects.get(product_id=4)
    chocolate_ingredients = Ingredient.objects.filter(product=1)
    banana_ingredients = Ingredient.objects.filter(product=2)
    strawberry_ingredients = Ingredient.objects.filter(product=3)
    cookies_and_cream_ingredients = Ingredient.objects.filter(product=4)

    context = {
        "chocolate_nutrition": chocolate_nutrition,
        "banana_nutrition": banana_nutrition,
        "strawberry_nutrition": strawberry_nutrition,
        "cookies_and_cream_nutrition": cookies_and_cream_nutrition,
        "chocolate_ingredients": chocolate_ingredients,
        "banana_ingredients": banana_ingredients,
        "strawberry_ingredients": strawberry_ingredients,
        "cookies_and_cream_ingredients": cookies_and_cream_ingredients,
    }

    return render(request, "products/product_detail.html", context)


def product_management(request):
    """
    Returns the product management page
    """
    return render(request, "products/product_management.html")


def admin_add(request):
    product_form = ProductForm()
    nutrition_form = NutritionForm()
    ingredient_form = IngredientForm()
    template = 'products/admin_add.html'
    context = {
        "product_form": product_form,
        "nutrition_form": nutrition_form,
        "ingredient_form": ingredient_form
    }
    return render(request, template, context)


def admin_edit(request):
    return render(request, "products/admin_edit.html")


def admin_delete(request):
    return render(request, "products/admin_delete.html")