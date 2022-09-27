from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    """
    Alters display in the django admin panel to show items in list_display
    """

    list_display = (
        "id",
        "user",
    )


admin.site.register(UserProfile, UserProfileAdmin)
