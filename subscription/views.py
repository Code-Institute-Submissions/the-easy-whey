from django.shortcuts import render

# Create your views here.
def subscribe(request):
    """
    Returns the subscription page
    """
    return render(request, "subscription/subscription.html")
