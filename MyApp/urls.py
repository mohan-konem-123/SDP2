from django.urls import path

from MyApp import views

urlpatterns = [
    path('',views.home , name="index"),
    path('about', views.about, name="about"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('contact-us', views.contact, name="contact-us"),
    path('shop', views.shop, name="shop"),
    path('addToCart', views.addToCart, name="addToCart")
]