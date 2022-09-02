from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages

from .forms import SubscriptionDetailsForm, SubscriptionItemsForm
from .actions import add_bag_quantites
from .models import Subscription, SubscriptionLineItem
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

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
            subscription_items_form = SubscriptionItemsForm()
            context = {
                "subscription_items_form": subscription_items_form,
            }
            request.session['save_information'] = 'save_information' in request.POST
            if request.session['save_information']:

                profile = get_object_or_404(UserProfile, user=request.user)
                profile.default_address_one = subscription_details_form.cleaned_data["address_one"]
                profile.default_address_two = subscription_details_form.cleaned_data["address_two"]
                profile.default_town_city = subscription_details_form.cleaned_data["town_city"]
                profile.default_postcode = subscription_details_form.cleaned_data["postcode"]
                profile.default_phone_number = subscription_details_form.cleaned_data["phone_number"]
                profile.default_county = subscription_details_form.cleaned_data["county"]
                profile.default_country = subscription_details_form.cleaned_data["country"]
                profile.save()

            return render(request, 'subscription/subscription_items.html', context)

    user_information = get_object_or_404(UserProfile, user=request.user)
    if hasattr(user_information, 'subscriptions'):
        messages.error(request, "You already have a subscription!")
        profile = get_object_or_404(UserProfile, user=request.user)
        form = UserProfileForm(instance=profile)
        subscription = profile.subscriptions
        context = {
            "form": form,
            "subscription": subscription,
        }
        return render(request, "profiles/profile.html", context)

    instance_data = {
        "phone_number": user_information.default_phone_number,
        "address_one": user_information.default_address_one,
        "address_two": user_information.default_address_two,
        "postcode": user_information.default_postcode,
        "town_city": user_information.default_town_city,
        "county": user_information.default_county,
        "country": user_information.default_country,
    }
    subscription_details_form = SubscriptionDetailsForm(initial=instance_data)
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

    if "subscription_number" not in request.session:
        messages.error(request, "An error occured, please try again.")
        return redirect(reverse('subscribe_details'))

    subscription_items_form = SubscriptionItemsForm()
    context = {
        "subscription_items_form": subscription_items_form,
    }
    return render(request, "subscription/subscription_items.html", context)


def payment(request):
    context = {}
    return render(request, "subscription/payment.html", context)