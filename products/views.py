from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
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

@login_required
def product_management(request):
    """
    Returns the product management page
    """
    return render(request, "products/product_management.html")

@login_required
def admin_add(request):
    if request.method == "POST":
        if "product_form_submit_button" in request.POST:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('admin_add'))
            else:
                return redirect(reverse('product_management'))
        if "nutrition_form_submit_button" in request.POST:
            form = NutritionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('admin_add'))
            else:
                return redirect(reverse('product_management'))
        if "ingredient_form_submit_button" in request.POST:
            form = IngredientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('admin_add'))
            else:
                return redirect(reverse('product_management'))
    else:
        product_form = ProductForm()
        nutrition_form = NutritionForm()
        ingredient_form = IngredientForm()
        # product = get_object_or_404(Product, pk=1)
        # print(product)
        # testtest = Product.objects.get(flavour='Chocolate Whey Protein')
        # print(testtest.id)
    template = 'products/admin_add.html'
    context = {
        "product_form": product_form,
        "nutrition_form": nutrition_form,
        "ingredient_form": ingredient_form
    }
    return render(request, template, context)


def admin_edit_list(request): 
    items = Product.objects.all()
    template = 'products/admin_edit_list.html'
    context = {
        "items": items
    }
    return render(request, template, context)


def admin_edit_item(request, item_id):
    item_product = get_object_or_404(Product, id=item_id)
    item_nutrition = get_object_or_404(Nutrition, product_id=item_id)
    # item_ingredients = Ingredient.objects.filter(product=1)
    if request.method == "POST":
        if "product_form_edit_button" in request.POST:
            form = ProductForm(request.POST, instance=item_product)
            if form.is_valid():
                form.save()
                return redirect(reverse('admin_edit_list'))
            else:
                return redirect(reverse('product_management'))
        if "nutrition_form_edit_button" in request.POST:
            form = NutritionForm(request.POST, instance=item_nutrition)
            if form.is_valid():
                form.save()
                return redirect(reverse('admin_edit_list'))
            else:
                return redirect(reverse('product_management'))
    template = 'products/admin_edit_item.html'
    product_form = ProductForm(instance=item_product)
    nutrition_form = NutritionForm(instance=item_nutrition)
    # ingredients_form = IngredientForm(instance=item_ingredients)
    context = {
        "product_form": product_form,
        "nutrition_form": nutrition_form,
        # "ingredients_form": ingredients_form,
    }

# Ingredient.objects.filter(product=1)
# for item in all:
#   print(item.name)
# this prints all the names out at least...

    return render(request, template, context)


def admin_delete(request):
    return render(request, "products/admin_delete.html")