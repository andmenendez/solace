from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Practitioner(models.Model):
	account		= models.OneToOneField(User, related_name="practitioner", on_delete=models.CASCADE)

	verified	= models.BooleanField(default=False)

	first_name	= models.CharField(max_length=100)
	last_name	= models.CharField(max_length=100)
	
	email		= models.EmailField()
	phone		= models.IntegerField(blank=True)

	zipcode 	= models.IntegerField()

	created 	= models.DateTimeField(auto_now_add=True)
	updated_at 	= models.DateTimeField(auto_now=True)



	def createPractitioner(user, user_info):
		Practitioner.objects.create(
			account 	= user,
			first_name 	= user_info["first_name"],
			last_name 	= user_info["last_name"],
			email 		= user_info["email"],
			phone 		= user_info["phone"],
			zipcode 	= user_info["zipcode"]
			)
