from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import SubscriptionDetailsForm, SubscriptionItemsForm
from .actions import add_bag_quantites
from .models import Subscription, SubscriptionLineItem
from products.models import Product

# Create your views here.
def subscribe(request):
    """
    Returns the subscription page
    """

    if request.user.is_authenticated:
        return redirect(reverse('subscribe_details'))

    context = {}
    return render(request, "subscription/subscription.html", context)

def subscribe_details(request):

    if request.method == "POST":
        subscription_details_form = SubscriptionDetailsForm(request.POST)
        if subscription_details_form.is_valid():
            subscription_details_form.save()
            request.session['subscription_number'] = subscription_details_form.instance.subscription_number
            return render(request, 'subscription/subscription_items.html', {'subscription_number': request.session['subscription_number']})

    subscription_details_form = SubscriptionDetailsForm()
    context = {
        "subscription_details_form": subscription_details_form,
    }
    return render(request, "subscription/subscription_details.html", context)


def subscribe_items(request):
    if request.method == "POST":
        subscription_items_form = SubscriptionItemsForm(request.POST)
        if subscription_items_form.is_valid():
            subscription = Subscription.objects.get(subscription_number=request.session["subscription_number"])

            order_data = {
                "Chocolate Whey Protein" : subscription_items_form.cleaned_data['chocolate_quantity'],
                "Banana Whey Protein" : subscription_items_form.cleaned_data['banana_quantity'],
                "Strawberry Whey Protein" : subscription_items_form.cleaned_data['strawberry_quantity'],
                "Cookies & Cream Whey Protein" : subscription_items_form.cleaned_data['cookies_and_cream_quantity'],
            }

            for flavour, quantity in order_data.items():
                print(f"flavour:{flavour}, quantity: {quantity}")
                SubscriptionLineItem(subscription=subscription, product=Product.objects.get(flavour=flavour), quantity=quantity).save()

            context = {}

            return render(request, "subscription/payment.html", context)

    subscription_items_form = SubscriptionItemsForm()
    context = {
        "subscription_items_form": subscription_items_form,
    }
    return render(request, "subscription/subscription_items.html", context)


def payment(request):
    context = {}
    return render(request, "subscription/payment.html", context)