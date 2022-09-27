from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order, name="order"),
    path('order/details/', views.order_details, name="order_details"),
    path('order/items/', views.order_items, name="order_items"),
    path('order/payment/', views.payment, name="payment"),
    path(
        "create-checkout-session",
        views.create_checkout_session,
        name="create_checkout_session",
    ),
    path('stripe-success', views.stripe_success, name="stripe_success"),
    path('stripe-cancel', views.stripe_cancel, name="stripe_cancel"),
    path('try_again', views.try_again, name="try_again"),
]
