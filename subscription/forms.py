from django import forms
from .models import Order, OrderLineItem
from django.forms.widgets import DateInput

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ("product", "order_number", "date", "total_cost", "is_paid", "user_profile",)


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

    chocolate_quantity = forms.IntegerField(label="How many bags of Chocolate Whey Protein would you like?", min_value=0, max_value=10, initial=0)
    banana_quantity = forms.IntegerField(label="How many bags of Banana Whey Protein would you like?", min_value=0, max_value=10, initial=0)
    strawberry_quantity = forms.IntegerField(label="How many bags of Strawberry Whey Protein would you like?", min_value=0, max_value=10, initial=0)
    cookies_and_cream_quantity = forms.IntegerField(label="How many bags of Cookies and Cream Whey Protein would you like?", min_value=0, max_value=10, initial=0)
