from django.db import models
from django.contrib.auth.models import User
from datamodels.models import *

# Create your models here.
# VERIFICATION
# https://www.healthguideusa.org/counselor_license_lookup.htm
# https://www.asppb.net/page/LicenseLookup

class Practitioner(models.Model):
	account				= models.OneToOneField(User, related_name="practitioner", on_delete=models.CASCADE)

	verified			= models.BooleanField(default=False)

	available 			= models.DateTimeField(null=True, blank=True)

	first_name			= models.CharField(max_length=100)
	last_name			= models.CharField(max_length=100)
	
	email				= models.EmailField()
	phone				= models.IntegerField(null=True, blank=True)

	accreditation		= models.CharField(max_length=100, null=True, blank=True)
	license 			= models.CharField(max_length=100,  null=True, blank=True)
	is_remote			= models.BooleanField(default=False)
	
	state 				= models.CharField(max_length=2, null=True, blank=True)
	zipcode 			= models.IntegerField(null=True, blank=True)

	school 				= models.CharField(max_length=200, null=True, blank=True)

	about 				= models.TextField(null=True, blank = True)

	created 			= models.DateTimeField(auto_now_add=True)
	updated_at 			= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.first_name + " " + self.last_name

	def to_char(self):
		return "PR"

	# GET METHODS

	# self.get_DATAMODELs
	# RETURNs [ARRAY] OF IDs
	def get_languages(self):
		return [str(language.getId()) for language in self.account.languages.all()]
	def get_focus_issues(self):
		return [focus_issue.getId() for focus_issue in self.account.focus_issues.all()]
	def get_specialties(self):
		return [specialty.getId() for specialty in self.account.specialties.all()]
	def get_approaches(self):
		return [approach.getId() for approach in self.account.approaches.all()]

	# self.get_DATAMODELs_array
	# RETURNs [ARRAY] OF data.__str__()
	def get_languages_array(self):
		return [str(LanguageData.objects.get(id=id)) for id in self.get_languages()]
	def get_focus_issues_array(self):
		return [str(FocusIssueData.objects.get(id=id)) for id in self.get_focus_issues()]
	def get_specialties_array(self):
		return [str(SpecialtyData.objects.get(id=id)) for id in self.get_specialties()]
	def get_approaches_array(self):
		return [str(ApproachData.objects.get(id=id)) for id in self.get_approaches()]

	# self.read_DATAMODELs
	# RETURNs string OF data.__str__() divided by ', '
	def read_languages(self):
		return ', '.join([str(LanguageData.objects.get(id=id)) for id in self.get_languages()])
	def read_focus_issues(self):
		return ', '.join([str(FocusIssueData.objects.get(id=id)) for id in self.get_focus_issues()])
	def read_specialties(self):
		return ', '.join([str(SpecialtyData.objects.get(id=id)) for id in self.get_specialties()])
	def read_approaches(self):
		return ', '.join([str(ApproachData.objects.get(id=id)) for id in self.get_approaches()])


	# CONVENIENCE METHOD
	def createPractitioner(user, user_info):
		Practitioner.objects.create(
			account 	= user,
			first_name 	= user_info["first_name"],
			last_name 	= user_info["last_name"],
			email 		= user_info["email"],
			phone 		= user_info["phone"],
			zipcode 	= user_info["zipcode"]
			)
