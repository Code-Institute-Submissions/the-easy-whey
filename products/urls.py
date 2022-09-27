from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('product/', views.product_detail, name="product_detail"),
    path('product/admin/', views.product_management,
         name="product_management"),
    path('product/admin/add/', views.admin_add, name="admin_add"),
    path('product/admin/edit/item/<item_id>', views.admin_edit_item,
         name="admin_edit_item"),
    path('product/admin/edit/item/<item_id>/ingredient/<ingredient_id>',
         views.admin_edit_item_ingredient, name="admin_edit_item_ingredient"),
    path('product/admin/edit/', views.admin_edit_list, name="admin_edit_list"),
    path('product/admin/edit/item/delete_ingredient/<ingredient_id>',
         views.delete_ingredient, name="delete_ingredient"),
    path('product/admin/edit/delete/<item_id>',
         views.admin_delete, name="admin_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
