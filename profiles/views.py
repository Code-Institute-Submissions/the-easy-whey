from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile
from subscription.models import Subscription


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

    if hasattr(profile, 'subscriptions'):
        subscription = profile.subscriptions
        context = {
            "form": form,
            "subscription": subscription,
        }
    else:
        context = {
            "form": form,
        }
    
    return render(request, "profiles/profile.html", context)


@login_required
def subscription_history(request, subscription_number):
    
    subscription = get_object_or_404(Subscription, subscription_number=subscription_number)

    if request.user == subscription.user_profile.user:
        messages.info(request, "This is a previous subscription.")

        template = 'profiles/view_subscription.html'
        context = {
            "subscription": subscription
        }

        return render(request, template, context)
        
    if request.user != subscription.user_profile.user:
        messages.error(request, "An error occured.")
        return redirect(reverse('profile'))

def delete_subscription(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    subscription = profile.subscriptions
    subscription.delete()
    messages.success(request, "Your subscription has been cancelled.")
    return redirect(reverse('profile'))