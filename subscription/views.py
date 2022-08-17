from django.shortcuts import render
from django.contrib import messages

from .forms import SubscriptionForm

# Create your views here.
def subscribe(request):
    """
    Returns the subscription page
    """

    subscription_form = SubscriptionForm()
    context = {
        "subscription_form" : subscription_form,
    }
    return render(request, "subscription/subscription.html", context)
