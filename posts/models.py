from django.db import models
# from clients.models import Client
# from practitioners.models import Practitioner
# Create your models here.

class Anon_Post(models.Model):
	title 		= models.CharField(max_length=100)
	body 		= models.TextField()
	
	created = models.DateTimeField(auto_now_add=True)

class Temp_Client(models.Model):
	contact_id	= models.CharField(max_length=100)
	post 		= models.ForeignKey(Anon_Post, on_delete=models.CASCADE)

	created = models.DateTimeField(auto_now_add=True)
	
# class TC_connect(models.Model):
	# practitioner 	= models.ForeignKey(Practitioner, on_delete=models.CASCADE, related_name= "practitioner")
	# client 			= models.ForeignKey(Client, on_delete=models.CASCADE, related_name= "client")	

	# created = models.DateTimeField(auto_now_add=True)