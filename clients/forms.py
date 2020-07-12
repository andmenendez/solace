from django import forms
import datetime
from .models import Client

# ANONYMOUS POSTING
# form takes all information, controller creates both the a_post and the temp user
class AnonForm(forms.Form):
	title 	= forms.CharField(max_length=100)
	body 		= forms.CharField(widget=forms.Textarea)
	contact_id 	= forms.CharField(max_length=100)
	is_public 	= forms.BooleanField( required=False)


# CLIENT LOGIN
# login and registration/info update
class ClientLoginForm(forms.Form):
	username	= forms.CharField()
	password	= forms.CharField(max_length=50, widget=forms.PasswordInput)

class ClientInfoForm(forms.Form):
	class Meta:
		model = Client
		exclude = ('created')

	username	= forms.CharField(max_length=100)
	password	= forms.CharField(max_length=50, widget=forms.PasswordInput)
	password_c	= forms.CharField(max_length=50, widget=forms.PasswordInput)

	first_name	= forms.CharField(max_length=100)
	last_name	= forms.CharField(max_length=100)
	birthday	= forms.DateField(initial=datetime.date.today)
	
	email		= forms.EmailField()
	phone		= forms.IntegerField()
	zipcode 	= forms.IntegerField()
