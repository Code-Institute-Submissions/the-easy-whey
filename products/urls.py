from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('product/', views.product_detail, name="product_detail"),
    path('product/admin/', views.product_management, name="product_management"),
]
