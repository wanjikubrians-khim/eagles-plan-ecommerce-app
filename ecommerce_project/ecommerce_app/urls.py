from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart_view, name='cart'),  # Keep only this
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
