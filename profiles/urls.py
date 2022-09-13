from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('profile/<subscription_number>', views.subscription_history, name="subscription_history"),
    path('delete_subscription', views.delete_subscription, name="delete_subscription"),
]
