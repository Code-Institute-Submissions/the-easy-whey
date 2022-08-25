from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
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
    
    chocolate_nutrition = Nutrition.objects.get(product__flavour="Chocolate Whey Protein")
    banana_nutrition = Nutrition.objects.get(product__flavour="Banana Whey Protein")
    strawberry_nutrition = Nutrition.objects.get(product__flavour="Strawberry Whey Protein")
    cookies_and_cream_nutrition = Nutrition.objects.get(product__flavour="Cookies & Cream Whey Protein")
    chocolate_ingredients = Ingredient.objects.filter(product__flavour="Chocolate Whey Protein")
    banana_ingredients = Ingredient.objects.filter(product__flavour="Banana Whey Protein")
    strawberry_ingredients = Ingredient.objects.filter(product__flavour="Strawberry Whey Protein")
    cookies_and_cream_ingredients = Ingredient.objects.filter(product__flavour="Cookies & Cream Whey Protein")
    
    # all_data = {
    #     "chocolate_info": [chocolate_nutrition, chocolate_ingredients],
    #     "banana_info": [banana_nutrition, banana_ingredients],
    #     "strawberry_info": [strawberry_nutrition, strawberry_ingredients],
    #     "cookies_and_cream_info": [cookies_and_cream_nutrition, cookies_and_cream_ingredients],
    # }
    # COMMENTS ADDED - THIS PRODUCT HAS ALL OF THE NUTRITION AND INGREDIENT DATA ATTACHED TOO! CAN USE THIS. SEE TEMPLATE.
    context = {
        "products": Product.objects.all()
    }

    return render(request, "products/product_detail.html", context)

@login_required
@staff_member_required
def product_management(request):
    """
    Returns the product management page
    """
    return render(request, "products/product_management.html")

@login_required
@staff_member_required
def admin_add(request):
    if request.method == "POST":
        if "product_form_submit_button" in request.POST:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Successfully added Product!")
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

    template = 'products/admin_add.html'
    context = {
        "product_form": product_form,
        "nutrition_form": nutrition_form,
        "ingredient_form": ingredient_form
    }
    return render(request, template, context)

@login_required
@staff_member_required
def admin_edit_list(request): 
    items = Product.objects.all()
    template = 'products/admin_edit_list.html'
    context = {
        "items": items
    }
    return render(request, template, context)

@login_required
@staff_member_required
def admin_edit_item(request, item_id):
    item_product = False
    try:
        item_product = Product.objects.get(id=item_id)
    except:
        print("Item not found - Product")
    item_nutrition = False
    try:
        item_nutrition = Nutrition.objects.get(product_id=item_id)
    except:
        print("Item not found - Nutrition")
    item_ingredients = False
    try:
        item_ingredients = Ingredient.objects.filter(product__id=item_id)
    except:
        print("Item not found - Ingredients")
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
        if "ingredients_form_edit_button" in request.POST:
            # HOW TO HANDLE THIS PROPERLY? NOW THERE ARE MULTIPLE INSTANCES...? MATS SUGGESTION TO DO LIKE A LIST OF ALL THE INGREDIENTS WITH EDIT OR DELETE BUTTONS.
            form = IngredientForm(request.POST, instance=item_ingredients)
            if form.is_valid():
                form.save()
                return redirect(reverse('admin_edit_list'))
            else:
                return redirect(reverse('product_management'))
          
    template = 'products/admin_edit_item.html'
    
    context = {}
    ingredient_forms = []
    if item_product:
        product_form = ProductForm(instance=item_product)
        context["product_form"] = product_form
    if item_nutrition:
        nutrition_form = NutritionForm(instance=item_nutrition)
        context["nutrition_form"] = nutrition_form
    if item_ingredients:
        for ingredient in item_ingredients:
            ingredient_forms.append(IngredientForm(instance=ingredient))
    
    context["ingredient_forms"] = ingredient_forms


    #     ingredients_form = IngredientForm(instance=item_ingredients)
    #     context["ingredients_form"] = ingredients_form

    return render(request, template, context)

@login_required
@staff_member_required
def admin_delete(request, item_id):
    item = get_object_or_404(Product, id=item_id)
    item.delete()
    return render(request, "products/product_management.html")