from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

# Create your views here.
def contact(request):
    """
    Returns the contact page
    """
    contact_form = ContactForm()
    context = {
        "form": contact_form
    }
    return render(request, "contact/contact.html", context)

def message_management(request):
    all_messages = Contact.objects.all()
    context = {
        "all_messages" : all_messages
    }
    return render(request, "contact/all_messages.html", context)

def admin_view_message(request):
    pass

def admin_delete_message(request):
    pass