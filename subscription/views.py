from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import SubscriptionDetailsForm, SubscriptionItemsForm
from .actions import add_bag_quantites

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
            # chocolate_quantity = subscription_details_form.cleaned_data['chocolate_quantity']
            # banana_quantity = subscription_details_form.cleaned_data['banana_quantity']
            # strawberry_quantity = subscription_details_form.cleaned_data['strawberry_quantity']
            # cookies_quantity = subscription_details_form.cleaned_data['cookies_quantity']
            subscription_details_form.save()
            # print(add_bag_quantites(chocolate_quantity, banana_quantity, strawberry_quantity, cookies_quantity))
            return redirect(reverse('subscribe_items'))

    subscription_details_form = SubscriptionDetailsForm()
    context = {
        "subscription_details_form": subscription_details_form,
    }
    return render(request, "subscription/subscription_details.html", context)


def subscribe_items(request):

    subscription_items_form = SubscriptionItemsForm()
    context = {
        "subscription_items_form": subscription_items_form,
    }
    return render(request, "subscription/subscription_items.html", context)