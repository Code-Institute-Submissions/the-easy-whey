from django.shortcuts import render

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
    return render(request, "products/product_detail.html")


def product_management(request):
    """
    Returns the product management page
    """
    return render(request, "products/product_management.html")