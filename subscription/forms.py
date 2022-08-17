from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ("name","email","phone_number","address_one","address_two","town_city","county","postcode", "country",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name" : "Full Name",
            "email" : "Email Address",
            "phone_number" : "Phone Number",
            "address_one" : "Street Address 1",
            "address_two" : "Street Address 2",
            "town_city" : "Town or City",
            "county" : "County",
            "postcode" : "Postcode",
            "country" : "Country",

        }
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
        self.fields["name"].widget.attrs["autofocus"] = True
