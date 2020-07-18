from django import forms
import datetime

# ANONYMOUS POSTING
# form takes all information, controller creates both the a_post and the temp user
class AnonForm(forms.Form):
	title 	= forms.CharField(max_length=100)
	body 		= forms.CharField(widget=forms.Textarea)
	contact_id 	= forms.CharField(max_length=100)
	is_public 	= forms.BooleanField( required=False)
