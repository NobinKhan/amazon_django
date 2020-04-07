from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,ListView
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.utils import timezone
from django.contrib import messages
from .forms import CheckoutForm
from .models import Product,OrderProduct,Order
# Create your views here.

class HomeView(ListView):
	model = Product
	template_name = 'home.html'

class ShopView(ListView):
	model = Product
	template_name = 'shop.html'

class ProductDetailView(DetailView):
	model = Product
	template_name = 'product_detail.html'


class CartView(View):
	def get(self,request,*args,**kwargs):
		try:
			order = Order.objects.get(user=self.request.user,ordered=False)
			context = {
				'object': order,
			}
			return render(self.request,'cart.html',context)
		except ObjectDoesNotExist:
			messages.error(self.request,'You do not have active order')
			return redirect("/")

class CheckoutView(View):
	def get(self,request,*args,**kwargs):
		try:
			order = Order.objects.get(user=self.request.user,ordered=False)
			form = CheckoutForm()
			context = {
				'order': order,
				'forms': form,
			}
			return render(self.request,'checkout.html',context)
		except ObjectDoesNotExist:
			messages.error(self.request,'You do not have active order')
			return redirect("/")



def add_to_cart(request,slug):
	#get the product.
	take_product = get_object_or_404(Product, slug=slug)
	#create order product.
	create_order_product, created = OrderProduct.objects.get_or_create(
		item = take_product,
		user = request.user,
		ordered = False
	)
	#create_order_product.save()
	order_qs = Order.objects.filter(user = request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		order_check = order.items.filter(item__slug = take_product.slug)
		#check if the order item is in the order.
		if create_order_product in order_check:
			create_order_product.quantity += 1
			create_order_product.save()
			messages.info(request,"This item quantity was updated")
			return redirect('core_main:cart')
		else:
			order.items.add(create_order_product)
			messages.info(request,"This inner item was added to your cart")
			return redirect('core_main:cart')
	else:
		date_of_order = timezone.now()
		order_var = Order.objects.create(user=request.user,ordered_date=date_of_order)
		order_var.items.add(create_order_product)
		messages.info(request,"This item was added to your cart")
	return redirect('core_main:cart')


def remove_from_cart(request,slug):
	#get_the_item
	take_product = get_object_or_404(Product, slug=slug)
	#return queryset
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		order_check = order.items.filter(item__slug = take_product.slug)
		order_item_query = OrderProduct.objects.filter(
				item=take_product,
				user=request.user,
				ordered=False
			)[0]
		if order_item_query in order_check:
			order.items.remove(order_item_query)
			messages.info(request,"This item removed from  your cart")
			return redirect("core_main:cart")
		else:
			messages.info(request,"This item was not in your cart")
			return redirect("core_main:cart")

	else:
		messages.info(request,"you do not have active order")
		return redirect("core_main:cart")


def remove_single_item_from_cart(request,slug):
	#get the item.
	take_product = get_object_or_404(Product, slug=slug)
	#return queryset
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		order_check = order.items.filter(item__slug = take_product.slug)
		order_item_query = OrderProduct.objects.filter(
				item=take_product,
				user=request.user,
				ordered=False
			)[0]

		if order_item_query.quantity > 1:
			order_item_query.quantity -= 1
			order_item_query.save()
			messages.info(request,"One item was removed from your cart")
			return redirect("core_main:cart")
		else:
			order.items.remove(order_item_query)
			messages.info(request,"This item was not in your cart")
			return redirect("core_main:cart")
	else:
		messages.info(request,"you do not have active order")
		return redirect("core_main:cart")





def contact_view(request):
	return render(request,'contact.html')

def about_view(request):
	return render(request,'about.html')

def blog_view(request):
	return render(request,'blog.html')