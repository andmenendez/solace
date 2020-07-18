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

	username	= forms.CharField(max_length=100)
	password	= forms.CharField(max_length=50, widget=forms.PasswordInput)
	password_c	= forms.CharField(max_length=50, widget=forms.PasswordInput)

	first_name	= forms.CharField(max_length=100)
	last_name	= forms.CharField(max_length=100)
	birthday	= forms.CharField(min_length=10, max_length=10, 
		widget=forms.TextInput(attrs={'placeholder':'MM/DD/YYYY'}))
	
	email		= forms.EmailField()
	phone		= forms.IntegerField()
	zipcode 	= forms.IntegerField()


