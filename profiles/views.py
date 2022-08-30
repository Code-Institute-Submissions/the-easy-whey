from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def profile(request):
    """
    Returns the profile page
    """
    context = {}
    return render(request, "profiles/profile.html", context)
