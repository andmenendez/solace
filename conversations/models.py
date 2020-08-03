from django.db 					import models
from clients.models 			import Client 
from posts.models 				import Temp_Client
from practitioners.models 		import Practitioner
from django.contrib.auth.models import User

class Conversation(models.Model):
	client 	 		= models.ForeignKey(Client, on_delete=models.CASCADE)
	practitioner  	= models.ForeignKey(Practitioner, on_delete=models.CASCADE)

	created 		= models.DateTimeField(auto_now_add=True)
	updated_at 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.client + " & " + self. practitioner

	def send_message(self, author, text):
		Message.objects.create(author=author, body=text, conversation=self)

class Message(models.Model):
	author 			= models.ForeignKey(User, on_delete=models.CASCADE)
	body 			= models.CharField(max_length=200)
	conversation 	= models.ForeignKey(Conversation, on_delete=models.CASCADE)
	created 		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return ">> " + self.body

class AnonConversation(models.Model):
	temp_client 	= models.ForeignKey(Temp_Client, on_delete=models.CASCADE, related_name="anon_conversations")
	practitioner  	= models.ForeignKey(Practitioner, on_delete=models.CASCADE)

	created 		= models.DateTimeField(auto_now_add=True)
	updated_at 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.temp_client.contact_id

	def send_message(self, author, text):
		AnonMessage.objects.create(author=author, body=text, conversation=self)

class AnonMessage(models.Model):
	author 			= models.CharField(max_length=2)
	body 			= models.CharField(max_length=200)
	conversation 	= models.ForeignKey(AnonConversation, on_delete=models.CASCADE, related_name="message_set")
	created 		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return ">> " + self.body

