from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Creates the contact form to be rendered
    """
    class Meta:
        model = Contact
        fields = "__all__"
