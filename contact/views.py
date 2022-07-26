from django.shortcuts import render

# Create your views here.
def contact(request):
    """
    Returns the contact page
    """
    return render(request, "contact/contact.html")
