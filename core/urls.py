from django.urls import path
from core.views import (
	HomeView,
	ShopView,
	ProductDetailView,
	add_to_cart,
	remove_from_cart,
	remove_single_item_from_cart,
	CartView,
	CheckoutView,
	AddCouponView,
	PaymentView,
	BikashView,
	DbblView,
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
    path('checkout/',CheckoutView.as_view(),name="checkout"),
    path('add-coupon/',AddCouponView.as_view(),name="add-coupon"),
    path('payment_stripe/<payment_option>/',PaymentView.as_view(),name="payment"),
    path('payment_bikash/<payment_option>/',BikashView.as_view(),name="bikash"),
    path('payment_dbbl/<payment_option>/',DbblView.as_view(),name="dbbl"),
    path('contact/', contact_view),
    path('about/', about_view),
    path('blog/', blog_view),  
]