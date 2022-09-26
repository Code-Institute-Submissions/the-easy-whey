from django import forms
from .models import Product, Nutrition, Ingredient

class ProductForm(forms.ModelForm):
    """
    Creates the product form to be rendered
    """
    class Meta:
        model = Product
        fields = '__all__'


class NutritionForm(forms.ModelForm):
    """
    Creates the nutrition form to be rendered
    """
    class Meta:
        model = Nutrition
        fields = '__all__'


class IngredientForm(forms.ModelForm):
    """
    Creates the ingredient form to be rendered
    """
    class Meta:
        model = Ingredient
        fields = '__all__'


class IngredientEditForm(forms.ModelForm):
    """
    Creates the ingredient form to be rendered
    """
    class Meta:
        model = Ingredient
        fields = ('name',)