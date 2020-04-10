from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse


ADDRESS_CHOICES = (
	('B', 'Billing'),
	('S', 'Shipping'),
)



class Product(models.Model):
	tag_name = models.CharField(max_length=20,blank=True,null=True)
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True,null=True)
	image = models.ImageField()
	price = models.DecimalField(decimal_places=2,max_digits=10)
	discount_price = models.DecimalField(decimal_places=2,max_digits=10)
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("core_main:product_detail",kwargs={
			'slug': self.slug
		})

	def get_add_to_cart_url(self):
		return reverse("core_main:add_to_cart",kwargs={
			'slug': self.slug
		})

	def get_remove_from_cart_url(self):
		return reverse("core_main:remove_from_cart",kwargs={
			'slug': self.slug
		})

	def get_remove_single_from_cart_url(self):
		return reverse("core_main:remove_single_item_from_cart",kwargs={
			'slug': self.slug
		})


class OrderProduct(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	item = models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.quantity} of {self.item.title}"

	def get_total_item_price(self):
		return self.quantity * self.item.price

	def get_total_discount_item_price(self):
		return self.quantity * self.item.discount_price


	def get_amount_saved(self):
		return self.get_total_item_price() - self.get_total_discount_item_price()

	def get_final_price(self):
		if self.item.discount_price:
			return self.get_total_discount_item_price()
		return self.get_total_item_price()
	

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ref_code = models.CharField(max_length=20,blank=True,null=True)
	items = models.ManyToManyField(OrderProduct)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	billing_address = models.ForeignKey(
		'Address', related_name='billing_address', on_delete=models.SET_NULL,blank=True,null=True)
	shipping_address = models.ForeignKey(
		'Address',related_name='shipping_address', on_delete=models.SET_NULL,blank=True,null=True)
	coupon = models.ForeignKey(
		'Cupon',on_delete=models.SET_NULL,blank=True,null=True)
	payment = models.ForeignKey(
		'Payment',on_delete=models.SET_NULL,blank=True,null=True)
	being_delivered = models.BooleanField(default=False)
	received = models.BooleanField(default=False)
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username
	"""
	def get_total(self):
		total = 0
		items_all = self.items.all()

		for order_item in items_all:
			total = total + order_item.get_final_price()
		if self.coupon:
			total -= self.coupon.amount
		return total
	"""
	def get_total(self):
		total = 0
		items_all = self.items.all()

		for order_item in items_all:
			total = total + order_item.get_final_price()
		if self.coupon:
			total -= self.coupon.amount
		return total

class Address(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	country = CountryField(multiple=False)
	street_address = models.CharField(max_length=100)
	apartment_address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	zip_code = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.EmailField()
	address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
	default = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural = 'Addresses'


class Payment(models.Model):
	stripe_charge_id = models.CharField(max_length=50)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)
	amount = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username



class Cupon(models.Model):
	code = models.CharField(max_length=20)
	amount = models.DecimalField(decimal_places=2,max_digits=10)

	def __str__(self):
		return self.code


	