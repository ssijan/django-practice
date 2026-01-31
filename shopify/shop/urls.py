from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("search/", views.search, name="search"),
    path("cart/", views.cart_details, name = 'cart'),
    path('about/', views.about, name='AboutUs'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='AddToCart'),
    path('increase-cart/<int:product_id>/', views.increase_cart, name = 'IncreaseCart'),
    path('decrease-cart/<int:product_id>/', views.decrease_cart, name = 'DecreaseCart'),
    path('remove-cart/<int:product_id>/', views.remove_cart, name = 'Remove')
]