from django import forms
import datetime
from .models import Client

# CLIENT LOGIN
# login and registration/info update
class ClientLoginForm(forms.Form):
	username	= forms.CharField()
	password	= forms.CharField(max_length=50, widget=forms.PasswordInput)

class ClientInfoForm(forms.Form):
	class Meta:
		model = Client
		exclude = ('created', 'updated_at')

	email		= forms.EmailField()

	username	= forms.CharField(max_length=100)
	password	= forms.CharField(max_length=50, widget=forms.PasswordInput)
	password_c	= forms.CharField(max_length=50, widget=forms.PasswordInput)

	first_name	= forms.CharField(max_length=100, required=False)
	last_name	= forms.CharField(max_length=100, required=False)
	birthday	= forms.CharField(min_length=10, max_length=10, 
		widget=forms.TextInput(attrs={'placeholder':'MM/DD/YYYY'}), required=False)
	
	phone		= forms.IntegerField(required=False)
	zipcode 	= forms.IntegerField(required=False)


