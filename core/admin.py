from django.contrib import admin
from .models import Product,OrderProduct,Order,Address,Cupon,Payment



class OrderAdmin(admin.ModelAdmin):
	list_display = [
		'user',
		'ordered',
		'shipping_address',
		'billing_address',
		'being_delivered',
		'received',
		'payment',
		'coupon'
	]
	list_display_links = [
		'user',
		'shipping_address',
		'billing_address',
		'payment',
		'coupon'
	]

	list_filter = [
		'ordered',
		'being_delivered',
		'received',
		
	]
	search_fields = [
		'user__username',
		'ref_code'
	]
	


class AddressAdmin(admin.ModelAdmin):
	list_display = [
		'user',
		'country',
		'street_address',
		'apartment_address',
		'city',
		'phone',
		'email',
		'zip_code',
		'address_type',
		'default'
	]
	list_filter = [
		'address_type',
		'default',
		'country',
	]
	search_fields = [
		'user__username',
		'street_address',
		'apartment_address',
		'zip_code',
	]



admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(Order,OrderAdmin)
admin.site.register(Address,AddressAdmin)

admin.site.register(Cupon)
admin.site.register(Payment)
