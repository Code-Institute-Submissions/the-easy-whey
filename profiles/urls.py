from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('profile/<order_number>', views.order_history, name="order_history"),
    path('delete_order', views.delete_order, name="delete_order"),
]
