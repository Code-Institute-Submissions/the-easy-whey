from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('contact/admin/', views.message_management, name="message_management"),
    path('contact/admin/<item_id>', views.admin_view_message, name="admin_view_message"),
    path('contact/admin/delete/<item_id>', views.admin_delete_message, name="admin_delete_message"),
]
