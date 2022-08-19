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
    instance_details = {
        "subscription": 1,
    }
    subscription_items_form = SubscriptionItemsForm(initial=instance_details)
    context = {
        "subscription_items_form": subscription_items_form,
    }
    print(request.session["subscription_number"])
    return render(request, "subscription/subscription_items.html", context)