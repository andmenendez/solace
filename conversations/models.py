from django.db import models

# Create your models here.
from clients.models import Client 
from practitioners.models import Practitioner


class Conversation(models.Model):
	client 	 		= models.OneToOneField(Client, on_delete=models.CASCADE)
	practitioner  	= models.OneToOneField(Practitioner, on_delete=models.CASCADE)

	created 		= models.DateTimeField(auto_now_add=True)
	updated_at 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return "Conversation between users: " + self.client.account.username + " & " + self.practitioner.account.username

	def send_message(self, author, text):
		Message.objects.create(author=author, body=text, conversation=self)

	def message_or_create(request):
		client = request.user.client
		practitioner = Practitioner.objects.get(pk=request.headers["Referer"].split("/")[-1])
		message = request.POST.get("message")

		try:
			conversation = Conversation.objects.get(client=client, practitioner=practitioner)

		except Conversation.DoesNotExist:

			convo = Conversation.objects.create(client=client, practitioner=practitioner)
			convo.save()
			convo.send_message(client, message)


class Message(models.Model):
	author 			= models.CharField(max_length=2, choices=[("CL", "Client"), ("PR", "Practitioner")])
	body 			= models.CharField(max_length=200)
	conversation 	= models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True)
	created 		= models.DateTimeField(auto_now_add=True)
