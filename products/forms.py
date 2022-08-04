from django import forms
from .models import Product, Nutrition, Ingredient

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class NutritionForm(forms.ModelForm):

    class Meta:
        model = Nutrition
        fields = '__all__'


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = '__all__'