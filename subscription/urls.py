from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name="subscribe"),
    path('subscribe/details', views.subscribe_details, name="subscribe_details"),
    path('subscribe/items', views.subscribe_items, name="subscribe_items"),
    path('subscribe/payment', views.payment, name="payment"),
    path('create-checkout-session', views.create_checkout_session, name="create_checkout_session"),
]
