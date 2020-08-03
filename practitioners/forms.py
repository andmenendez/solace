from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.forms import USStateField, USZipCodeField

# https://github.com/django/django-localflavor
from django import forms
import datetime
from .models import Practitioner
from datamodels.models import *

# PRACT LOGIN
# login and registration/info update
class PractLoginForm(forms.Form):
	class Meta: 
		fields = ["username","password"]

	username	= forms.CharField()
	password	= forms.CharField(max_length=50, widget=forms.PasswordInput)

class PractInfoForm(forms.Form):
	class Meta:
		model = Practitioner
		# fields = ["username","password","password_c","first_name","last_name","email","phone","zipcode"]
		exclude = ('available','verified', 'created', 'updated_at')

	username	= forms.CharField(max_length=100)
	password	= forms.CharField(max_length=50, widget=forms.PasswordInput)
	password_c	= forms.CharField(max_length=50, widget=forms.PasswordInput)

	first_name	= forms.CharField(max_length=100)
	last_name	= forms.CharField(max_length=100)
	
	email		= forms.EmailField()
	phone		= forms.IntegerField(required=False)
	# state 		= forms.ChoiceField(choices=STATE_CHOICES)  

	state = USStateField(required=False)
	zipcode = USZipCodeField(required=False)


class PractProfileForm(forms.ModelForm):
	class Meta:
		model = Practitioner
		exclude = ('account', 'available', 'verified','created', 'updated_at')
	phone 			= forms.IntegerField(required=False)
	accreditation 	= forms.CharField(required=False)
	license 		= forms.CharField(required=False)
	state 			= USStateField(required=False)
	zipcode 		= USZipCodeField(required=False)
	school 			= forms.CharField(required=False)
	about 			= forms.CharField(required=False, widget=forms.Textarea)

class PractMiscForm(forms.Form):
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super(PractMiscForm, self).__init__(*args, **kwargs)

		self.initial['languages'] 		= user.practitioner.get_languages()
		self.initial['focus_issues'] 	= user.practitioner.get_focus_issues()
		self.initial['specialties'] 	= user.practitioner.get_specialties()
		self.initial['approaches'] 		= user.practitioner.get_approaches()

	languages 	= forms.ModelMultipleChoiceField(
							widget = forms.CheckboxSelectMultiple,
							queryset=LanguageData.objects.all(),
							required=False, help_text="Language")

	focus_issues 	= forms.ModelMultipleChoiceField(
							widget = forms.CheckboxSelectMultiple,
								queryset=FocusIssueData.objects.all(), 
								required=False, help_text="Focus Issues")

	specialties 	= forms.ModelMultipleChoiceField(
							widget = forms.CheckboxSelectMultiple,
								queryset=SpecialtyData.objects.all(), 
								required=False, help_text="Specialties")

	approaches 		= forms.ModelMultipleChoiceField(
							widget = forms.CheckboxSelectMultiple,
								queryset=ApproachData.objects.all(), 
								required=False, help_text="Approaches")