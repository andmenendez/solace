from django import forms
import datetime
from .models import Practitioner

# PRACT LOGIN
# login and registration/info update
class PractLoginForm(forms.Form):
	username	= forms.CharField()
	password	= forms.CharField(max_length=50, widget=forms.PasswordInput)

class PractInfoForm(forms.Form):
	class Meta:
		model = Practitioner
		exclude = ('created', 'updated_at')

	username	= forms.CharField(max_length=100)
	password	= forms.CharField(max_length=50, widget=forms.PasswordInput)
	password_c	= forms.CharField(max_length=50, widget=forms.PasswordInput)

	first_name	= forms.CharField(max_length=100)
	last_name	= forms.CharField(max_length=100)
	
	email		= forms.EmailField()
	phone		= forms.IntegerField()

	zipcode 	= forms.IntegerField()