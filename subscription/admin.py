from django.contrib import admin
from .models import Subscription, SubscriptionLineItem

# Register your models here.

class SubscriptionLineItemAdminInline(admin.TabularInline):
    model = SubscriptionLineItem
    readonly_fields = ("product_total",)


class SubscriptionAdmin(admin.ModelAdmin):
    inlines = (SubscriptionLineItemAdminInline,)
    readonly_fields = ("subscription_number","date","total_cost","subscription_start_date", "subscription_end_date",)

    list_display = ("subscription_number","date","full_name","total_cost","subscription_start_date", "subscription_end_date",)

    ordering = ("-date",)

admin.site.register(Subscription, SubscriptionAdmin)