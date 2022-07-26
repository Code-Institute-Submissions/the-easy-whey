from django.shortcuts import render

# Create your views here.
def profile(request):
    """
    Returns the profile page
    """
    return render(request, "profiles/profile.html")
