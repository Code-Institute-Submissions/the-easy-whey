from django import forms
from django.core.exceptions import ValidationError
from .models import Order


class OrderDetailsForm(forms.ModelForm):
    """
    Creates the order details form to be rendered
    """

    class Meta:
        model = Order
        exclude = (
            "product",
            "order_number",
            "date",
            "total_cost",
            "is_paid",
            "user_profile",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "address_one": "Street Address 1",
            "address_two": "Street Address 2",
            "town_city": "Town or City",
            "county": "County",
            "postcode": "Postcode",
            "country": "County",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False


class OrderItemsForm(forms.Form):
    """
    Creates the order items form to be rendered
    """

    chocolate_quantity = forms.IntegerField(
        label="How many bags of Chocolate Whey Protein would you like?",
        min_value=0,
        max_value=10,
        initial=0,
    )
    banana_quantity = forms.IntegerField(
        label="How many bags of Banana Whey Protein would you like?",
        min_value=0,
        max_value=10,
        initial=0,
    )
    strawberry_quantity = forms.IntegerField(
        label="How many bags of Strawberry Whey Protein would you like?",
        min_value=0,
        max_value=10,
        initial=0,
    )
    cookies_and_cream_quantity = forms.IntegerField(
        label="How many bags of Cookies & Cream Whey Protein would you like?",
        min_value=0,
        max_value=10,
        initial=0,
    )

    def clean(self):
        cleaned_data = super().clean()
        chocolate_quantity_validation = cleaned_data["chocolate_quantity"]
        banana_quantity_validation = cleaned_data["banana_quantity"]
        strawberry_quantity_validation = cleaned_data["strawberry_quantity"]
        cookies_and_cream_validation = (
            cleaned_data["cookies_and_cream_quantity"]
            )
        total_quantities = [
            chocolate_quantity_validation,
            banana_quantity_validation,
            strawberry_quantity_validation,
            cookies_and_cream_validation,
        ]

        if sum(total_quantities) < 1:
            raise ValidationError("You cannot order nothing.")
        return cleaned_data
