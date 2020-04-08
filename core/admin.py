from django.contrib import admin
from .models import Product,OrderProduct,Order,Address,Cupon



class OrderAdmin(admin.ModelAdmin):
	list_display = [
		'user',
		'ordered',
		'shipping_address',
		'billing_address',
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



admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(Order,OrderAdmin)
admin.site.register(Address,AddressAdmin)

admin.site.register(Cupon)
