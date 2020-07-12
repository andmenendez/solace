from django.db import models

# Create your models here.

class Practitioner(models.Model):
	username	= models.CharField(max_length=100)
	password	= models.CharField(max_length=50)

	first_name	= models.CharField(max_length=100)
	last_name	= models.CharField(max_length=100)
	
	email		= models.EmailField()
	phone		= models.IntegerField(blank=True)

	zipcode 	= models.IntegerField()

	created = models.DateTimeField(auto_now_add=True)

