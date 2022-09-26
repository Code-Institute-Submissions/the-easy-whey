from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    """
    Alters display in the django admin panel to show items in list_display
    """
    list_display = ("id", "name", 'email', 'phone_number', 'message')


admin.site.register(Contact, ContactAdmin)
