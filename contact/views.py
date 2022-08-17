from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def contact(request):
    """
    Returns the contact page
    """
    return render(request, "contact/contact.html")
