from django.shortcuts import render
from .models import Product, Nutrition, Ingredient, Size
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
    products = Product.objects.all()
    nutrition = Nutrition.objects.all()
    chocolate_nutrition = Nutrition.objects.get(product_id = 1)

    context = {
        "products": products,
        "nutrition": nutrition,
        "chocolate": chocolate_nutrition
    }

    

    return render(request, "products/product_detail.html", context)


def product_management(request):
    """
    Returns the product management page
    """
    return render(request, "products/product_management.html")