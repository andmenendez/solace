from django.db import models

# Create your models here.


class A_post(models.Model):
	title 			= models.CharField(max_length=100)
	body 			= models.TextField()
	
	created = models.DateTimeField(auto_now_add=True)

class Temp_Client(models.Model):
	contact_id	= models.CharField(max_length=100)
	post 		= models.ForeignKey(A_post, on_delete=models.CASCADE)

	created = models.DateTimeField(auto_now_add=True)

class Client(models.Model):
	username	= models.CharField(max_length=100)
	password	= models.CharField(max_length=50)

	first_name	= models.CharField(max_length=100)
	last_name	= models.CharField(max_length=100)
	birthday	= models.DateField()
	
	email		= models.EmailField()
	phone		= models.IntegerField(blank=True)
	zipcode 	= models.IntegerField()

	created = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

