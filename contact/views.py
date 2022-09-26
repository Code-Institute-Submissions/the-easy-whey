from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import ContactForm
from .models import Contact

# Create your views here.


def contact(request):
    """
    Returns the contact page
    """
    request.session['checkout_key'] = False
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Successfully sent message!")

    context = {
        "form": contact_form
    }
    return render(request, "contact/contact.html", context)


@login_required
@staff_member_required
def message_management(request):
    """
    Returns page which contains all messages
    """
    all_messages = Contact.objects.all()
    context = {
        "all_messages": all_messages
    }
    return render(request, "contact/all_messages.html", context)


@login_required
@staff_member_required
def admin_view_message(request, message_id):
    """
    Returns a view of a single message that has been selected
    """
    message = Contact.objects.get(id=message_id)
    context = {
        "message": message
    }

    return render(request, "contact/view_message.html", context)


@login_required
@staff_member_required
def admin_delete_message(request, message_id):
    """
    Deletes a selected message
    """
    message = Contact.objects.get(id=message_id)
    message.delete()
    return redirect(reverse('message_management'))
