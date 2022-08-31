from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile


# Create your views here.
def profile(request):
    """
    Returns the profile page
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    subscriptions = profile.subscriptions.all()

    context = {
        "form": form,
        "subscriptions": subscriptions,
    }
    return render(request, "profiles/profile.html", context)
