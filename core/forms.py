from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
	('B','Bikash'),
	('S','Stripe'),
	('D','Dbbl'),
)

class CheckoutForm(forms.Form):
	#use for shipping address
	shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'form-control',
    }))
  
	shipping_address = forms.CharField(required=False)
	shipping_address2 = forms.CharField(required=False)
	shipping_city = forms.CharField(required=False)
	shipping_zip_code = forms.CharField(required=False)
	shipping_phone_number = forms.CharField(required=False)
	shipping_email_address = forms.EmailField(required=False)

	#use for billing address
	billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'form-control',
    }))

	billing_address = forms.CharField(required=False)
	billing_address2 = forms.CharField(required=False)
	billing_city = forms.CharField(required=False)
	billing_zip_code = forms.CharField(required=False)
	billing_phone_number = forms.CharField(required=False)
	billing_email_address = forms.EmailField(required=False)
	

	same_as_billing_address = forms.BooleanField(required=False)
	bill_to_different_address = forms.BooleanField(required=False)
	#set_default_billing = forms.BooleanField(required=False)
	#use_default_billing = forms.BooleanField(required=False)

	payment_option = forms.ChoiceField(
						widget=forms.RadioSelect,
						choices=PAYMENT_CHOICES
					)