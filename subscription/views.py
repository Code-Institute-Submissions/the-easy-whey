from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import SubscriptionDetailsForm, SubscriptionItemsForm
from .actions import add_bag_quantites
from .models import Subscription, SubscriptionLineItem

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
            # return redirect(reverse('subscribe_items'))
            return render(request, 'subscription/subscription_items.html', {'subscription_number': request.session['subscription_number']})

    subscription_details_form = SubscriptionDetailsForm()
    context = {
        "subscription_details_form": subscription_details_form,
    }
    return render(request, "subscription/subscription_details.html", context)


def subscribe_items(request):
# this formed rendered below like i thought, but need to get a custom form perhaps and add the quantities there? e.g. only shows 1 product box
# look into the subform / nested form stuff?
# print(request.session["subscription_number"]) - I NOW HAVE ACCESS TO THIS.

    if request.method == "POST":
        subscription_items_form = SubscriptionItemsForm(request.POST)
        if subscription_items_form.is_valid():
            chocolate_quantity = subscription_items_form.cleaned_data['chocolate_quantity']
            banana_quantity = subscription_items_form.cleaned_data['banana_quantity']
            strawberry_quantity = subscription_items_form.cleaned_data['strawberry_quantity']
            cookies_and_cream_quantity = subscription_items_form.cleaned_data['cookies_and_cream_quantity']
            subscription = Subscription.objects.get(subscription_number=request.session["subscription_number"])
            # item = Subscription.objects.get(subscription_number="9F1EDF0BBC444E84BAF93B577F45CBED") - ok so got the object here?
            # SubscriptionLineItem(subscription=item, product_id=1) gives me <SubscriptionLineItem: Product: Chocolate Whey Protein for the subscription: 9F1EDF0BBC444E84BAF93B577F45CBED
            # why does SubscriptionLineItem(subscription=item, product_id=1).quantity = 0, when in the admin view i see 2


            # GOT IT!
            # item = SubscriptionLineItem.objects.filter(subscription__subscription_number="9F1EDF0BBC444E84BAF93B577F45CBED") - THIS GETS THE OBJECTS, WHICH IS ALL 3 PRODUCTS IN THIS SUBSCRIPTION
            # item[0] then gets the first product, which is the Chocolate Whey Protein record
            # from here, simply using item[0].quantity gives me 2!!!!!
    subscription_items_form = SubscriptionItemsForm()
    context = {
        "subscription_items_form": subscription_items_form,
    }
    return render(request, "subscription/subscription_items.html", context)