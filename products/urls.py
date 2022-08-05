from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('product/', views.product_detail, name="product_detail"),
    path('product/admin/', views.product_management, name="product_management"),
    path('product/admin/add/', views.admin_add, name="admin_add"),
    path('product/admin/edit/<int:product_id>/', views.admin_edit, name="admin_edit"),
    path('product/admin/delete/', views.admin_delete, name="admin_delete"),
]
