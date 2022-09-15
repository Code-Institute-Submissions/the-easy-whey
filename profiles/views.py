from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile
from subscription.models import Order


# Create your views here.
@login_required
def profile(request):
    """
    Returns the profile page
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile saved.")

    form = UserProfileForm(instance=profile)

    if hasattr(profile, 'order'):
        order = profile.orders
        context = {
            "form": form,
            "order": order,
        }
    else:
        context = {
            "form": form,
        }
    
    return render(request, "profiles/profile.html", context)


@login_required
def order_history(request, order_number):
    
    order = get_object_or_404(Order, order_number=order_number)

    if request.user == order.user_profile.user:
        messages.info(request, "This is a previous order.")

        template = 'profiles/view_order.html'
        context = {
            "order": order
        }

        return render(request, template, context)
        
    if request.user != order.user_profile.user:
        messages.error(request, "An error occured.")
        return redirect(reverse('profile'))

def delete_order(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    order = profile.orders
    order.delete()
    messages.success(request, "Your order has been cancelled.")
    return redirect(reverse('profile'))