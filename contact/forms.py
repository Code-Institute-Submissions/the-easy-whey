from django import forms
from .models import Contact
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if "Kingsley" not in name:
            raise ValidationError("You have forgotten about Kingsley!")
        return name