from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
	account		= models.OneToOneField(User, related_name="client", on_delete=models.CASCADE)

	first_name	= models.CharField(max_length=100)
	last_name	= models.CharField(max_length=100)

	birthday	= models.CharField(max_length=10)
	
	email		= models.EmailField()
	phone		= models.IntegerField(blank=True)
	zipcode 	= models.IntegerField()

	created 	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.first_name + " " + self.last_name

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

