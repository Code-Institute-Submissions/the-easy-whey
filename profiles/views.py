from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    )
from subscription.models import Order
from .forms import UserProfileForm
from .models import UserProfile


# Create your views here.


@login_required
def profile(request):
    """
    Returns the profile page
    """
    request.session['checkout_key'] = False

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile saved.")

    orders = profile.orders.all()
    context = {
             "form": form,
             "orders": orders,
        }

    return render(request, "profiles/profile.html", context)


@login_required
def order_history(request, order_number):
    """
    Shows details of an order
    """
    order = get_object_or_404(Order, order_number=order_number)

    if request.user == order.user_profile.user:

        template = 'profiles/view_order.html'
        context = {"order": order}

        return render(request, template, context)

    if request.user != order.user_profile.user:
        messages.error(request, "An error occured.")
        return redirect(reverse('profile'))
