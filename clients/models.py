from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
	account		= models.OneToOneField(User, related_name="client", on_delete=models.CASCADE)
	email		= models.EmailField()

	first_name	= models.CharField(max_length=100, blank=True, null=True)
	last_name	= models.CharField(max_length=100, blank=True, null=True)

	birthday	= models.CharField(max_length=10, blank=True, null=True)
	
	phone		= models.IntegerField(blank=True, null=True)
	zipcode 	= models.IntegerField(blank=True, null=True)

	created 	= models.DateTimeField(auto_now_add=True, blank=True, null=True)
	updated_at 	= models.DateTimeField(auto_now=True, blank=True, null=True)

	def __str__(self):
		return self.first_name + " " + self.last_name

	def to_char(self):
		return "CL"
		
	def createClient(user, user_info):
		Client.objects.create(
			account 	= user,
			first_name 	= user_info["first_name"],
			last_name 	= user_info["last_name"],
			birthday 	= user_info["birthday"],
			email 		= user_info["email"],
			phone 		= user_info["phone"],
			zipcode 	= user_info["zipcode"]
			)

