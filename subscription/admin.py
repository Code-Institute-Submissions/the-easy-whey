from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Alters display in the django admin panel to show items in list_display
    """

    model = OrderLineItem
    readonly_fields = ("product_total",)


class OrderAdmin(admin.ModelAdmin):
    """
    Alters display in the django admin panel to show items in list_display
    """

    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        "order_number",
        "date",
        "total_cost",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "user_profile",
        "total_cost",
    )

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
