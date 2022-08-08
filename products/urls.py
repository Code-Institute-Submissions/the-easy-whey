from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('product/', views.product_detail, name="product_detail"),
    path('product/admin/', views.product_management, name="product_management"),
    path('product/admin/add/', views.admin_add, name="admin_add"),
    path('product/admin/edit/item/<item_id>', views.admin_edit_item, name="admin_edit_item"),
    path('product/admin/edit/', views.admin_edit_list, name="admin_edit_list"),
    path('product/admin/delete/', views.admin_delete, name="admin_delete"),
]
