from django.urls import path
from . import views

app_name="orders"
urlpatterns = [
    path('add_to_cart', views.add_to_cart, name="add_to_cart"),
    path('cart', views.cart, name="cart"),
    path('delete_from_cart', views.delete_from_cart, name="delete_from_cart"),
    path('delete_cart', views.delete_cart, name="delete_cart"),
    path('confirm_cart', views.confirm_cart, name="confirm_cart"),
    path('sendemail', views.sendemail, name="sendemail"),
]
