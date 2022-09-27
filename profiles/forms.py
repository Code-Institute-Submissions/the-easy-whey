from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Creates the form for the user profile to be created
    """

    class Meta:
        model = UserProfile
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "default_address_one": "Street Address 1",
            "default_address_two": "Street Address 2",
            "default_town_city": "Town or City",
            "default_postcode": "Postcode",
            "default_phone_number": "Phone Number",
            "default_county": "County",
            "default_country": "County",
        }

        self.fields["default_address_one"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False
