from django.db import models
# from clients.models import Client
# from practitioners.models import Practitioner
# Create your models here.

class Temp_Client(models.Model):
	contact_id	= models.EmailField()
	created 	= models.DateTimeField(auto_now_add=True)

	def to_char(self):
		return "TC"

	def __str__(self):
		return "Anonymous"

class Anon_Post(models.Model):
	body 		= models.TextField()
	
	author 		= models.ForeignKey(Temp_Client, on_delete=models.CASCADE, related_name="posts") 
	created 	= models.DateTimeField(auto_now_add=True)
