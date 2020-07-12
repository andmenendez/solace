from django.db import models
from clients.models import Client
from practitioners.models import Practitioner
# Create your models here.

class TC_connect(models.Model):
	practitioner 	= models.ForeignKey(Practitioner, on_delete=models.CASCADE, related_name= "practitioner")
	client 			= models.ForeignKey(Client, on_delete=models.CASCADE, related_name= "client")	

	created = models.DateTimeField(auto_now_add=True)