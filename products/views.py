from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Nutrition, Ingredient
from .forms import ProductForm, NutritionForm, IngredientEditForm, IngredientForm

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
    context = {
        "products": Product.objects.all(),
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
def admin_edit_item_ingredient(request, item_id, ingredient_id): 

    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    ingredient_form = IngredientEditForm(instance=ingredient)

    if request.method == "POST":
        form = IngredientEditForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited ingredient!")
            return redirect(reverse('admin_edit_item', args=[item_id]))
        else:
            return redirect(reverse('product_management'))

    template = 'products/admin_edit_item_ingredient.html'
    context = {
        "ingredient_form": ingredient_form,
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
            form = IngredientForm(request.POST, instance=item_ingredients)
            if form.is_valid():
                form.save()
                return redirect(reverse('admin_edit_list'))
            else:
                return redirect(reverse('product_management'))
          
    template = 'products/admin_edit_item.html'
    items = Ingredient.objects.filter(product_id=item_id)
    product_id = item_id

    context = {
        "items": items,
        "product_id": product_id,
        }
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

    return render(request, template, context)

@login_required
@staff_member_required
def admin_delete(request, item_id):
    item = get_object_or_404(Product, id=item_id)
    item.delete()
    messages.success(request, "Successfully deleted Product!")
    return render(request, "products/product_management.html")

@login_required
@staff_member_required
def delete_ingredient(request, ingredient_id):
    item = get_object_or_404(Ingredient, id=ingredient_id)
    item.delete()
    messages.success(request, "Successfully deleted ingredient!")
    return redirect(reverse('admin_edit_list'))
