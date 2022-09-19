from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
import stripe
from .forms import OrderDetailsForm, OrderItemsForm
from .actions import add_bag_quantites
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from django.contrib.sites.models import Site

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

def order(request):
    """
    Returns the order page
    """

    if request.user.is_authenticated:
        return redirect(reverse('order_details'))

    context = {}
    return render(request, "order/order.html", context)

def order_details(request):

    if request.method == "POST":
        order_details_form = OrderDetailsForm(request.POST)
        if order_details_form.is_valid():
            order_details_form.save()
            request.session['order_number'] = order_details_form.instance.order_number
            order_items_form = OrderItemsForm()
            context = {
                "order_items_form": order_items_form,
            }
            request.session['save_information'] = 'save_information' in request.POST
            if request.session['save_information']:

                profile = get_object_or_404(UserProfile, user=request.user)
                profile.default_address_one = order_details_form.cleaned_data["address_one"]
                profile.default_address_two = order_details_form.cleaned_data["address_two"]
                profile.default_town_city = order_details_form.cleaned_data["town_city"]
                profile.default_postcode = order_details_form.cleaned_data["postcode"]
                profile.default_phone_number = order_details_form.cleaned_data["phone_number"]
                profile.default_county = order_details_form.cleaned_data["county"]
                profile.default_country = order_details_form.cleaned_data["country"]
                profile.save()
                messages.success(request, "Your profile data has been updated.")

            return render(request, 'order/order_items.html', context)


    user_information = get_object_or_404(UserProfile, user=request.user)
    instance_data = {
        "phone_number": user_information.default_phone_number,
        "address_one": user_information.default_address_one,
        "address_two": user_information.default_address_two,
        "postcode": user_information.default_postcode,
        "town_city": user_information.default_town_city,
        "county": user_information.default_county,
        "country": user_information.default_country,
    }
    order_details_form = OrderDetailsForm(initial=instance_data)
    context = {
        "order_details_form": order_details_form,
    }
    return render(request, "order/order_details.html", context)


def order_items(request):
    if request.method == "POST":
        order_items_form = OrderItemsForm(request.POST)
        if order_items_form.is_valid():
            order = get_object_or_404(Order, order_number=request.session["order_number"])

            order_data = {
                "Chocolate Whey Protein" : order_items_form.cleaned_data['chocolate_quantity'],
                "Banana Whey Protein" : order_items_form.cleaned_data['banana_quantity'],
                "Strawberry Whey Protein" : order_items_form.cleaned_data['strawberry_quantity'],
                "Cookies & Cream Whey Protein" : order_items_form.cleaned_data['cookies_and_cream_quantity'],
            }

            for flavour, quantity in order_data.items():
                OrderLineItem(order=order, product=get_object_or_404(Product, flavour=flavour), quantity=quantity).save()

            context = {
                "order": order
            }
            return render(request, "order/payment.html", context)

    if "order_number" not in request.session:
        messages.error(request, "An error occured, please try again.")
        return redirect(reverse('order_details'))

    order_items_form = OrderItemsForm()
    context = {
        "order_items_form": order_items_form,
    }
    return render(request, "order/order_items.html", context)


def payment(request):
    context = {}
    return render(request, "order/payment.html", context)


def create_checkout_session(request):
    DOMAIN = Site.objects.get_current()
    order = get_object_or_404(Order, order_number=request.session["order_number"])
    order_lineitems = order.lineitems.all()
    items = []

    for item in order_lineitems:
        if item.quantity >= 1:
            items.append(
                {
                    'price_data': {
                        'currency': 'gbp',
                        'product_data': {
                            'name': item.product.flavour,
                        },
                        'unit_amount': 699,
                    },
                    'quantity': item.quantity,
                }
            )

    session = stripe.checkout.Session.create(
        customer_email=order.email,
        line_items=items,
        mode='payment',
        success_url=f"{DOMAIN}stripe-success",
        cancel_url=f"{DOMAIN}stripe-cancel",
    )
    
    return redirect(session.url, code=303)


def stripe_success(request):
    order = get_object_or_404(Order, order_number=request.session["order_number"])
    order.user_profile.user = request.user
    order.is_paid = True
    order.save()
    context = {
        "order": order
    }
    return render(request, "order/success.html", context)


def stripe_cancel(request):
    order = get_object_or_404(Order, order_number=request.session["order_number"])
    order.user_profile.user = request.user
    order.save()
    context = {
        "order": order
    }
    context = {}
    return render(request, "order/cancel.html", context)


def try_again(request):
    order = get_object_or_404(Order, order_number=request.session["order_number"])
    order.delete()
    return redirect(reverse('order'))