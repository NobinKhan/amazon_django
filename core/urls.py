from django.urls import path
from core.views import (
	HomeView,
	ShopView,
	ProductDetailView,
	add_to_cart,
	remove_from_cart,
	remove_single_item_from_cart,
	CartView,
	contact_view,
	about_view,
	blog_view
)

app_name = 'core_main'

urlpatterns = [
    path('', HomeView.as_view(),name="home_view"),
    path('shop/', ShopView.as_view(),name="shop_view"),
    path('product_detail/<slug>/',ProductDetailView.as_view(),name="product_detail"),
    path('add_to_cart/<slug>/',add_to_cart,name="add_to_cart"),
    path('remove_from_cart/<slug>/',remove_from_cart,name="remove_from_cart"),
    path('remove_single_item_from_cart/<slug>/',remove_single_item_from_cart,name="remove_single_item_from_cart"),
    path('cart/',CartView.as_view(),name="cart"),
    path('contact/', contact_view),
    path('about/', about_view),
    path('blog/', blog_view),  
]