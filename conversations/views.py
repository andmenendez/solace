from django.shortcuts 			import render
from django.http 				import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers

from django.contrib.auth.models import User
from practitioners.models 		import Practitioner
from clients.models 			import Client
from posts.models				import Temp_Client
from .models 					import Conversation

from .models import *

def show_conversation(request):

	# SEND MESSAGE REQUEST-INPUTS VIA POST (may be changed to GET)
	# 
	# show existing conversation and allow for message sending
	# 
	# RECIPIENT_CLASS 	(2-CHAR)
	# CONVERSATION_ID 	(CONVERSATION PK)
	# MESSAGE BODY 		(MESSAGE TEXT)
	# 

	if not request.user.is_authenticated:
		return HttpResponseNotFound("User not logged in")
	
	conversation_id	= request.POST.get("conversation_id")

	if conversation_id is None:
		client 			= request.user.client
		practitioner 	= Practitioner.objects.get(id = request.POST.get("pract_id"))
		conversation 	= Conversation.objects.create(client = client, practitioner = practitioner)
	else:
		conversation	= Conversation.objects.get(id=conversation_id)

	practitioner 	= conversation.practitioner
	client 			= conversation.client

	if request.user == practitioner.account:
		context = {
			"base_html":	'practitioners/base.html',
			"sender": 		practitioner,
			"recipient": 	client,
			"conversation":	conversation
		}
		return render(request, "conversations/conversation.html", context)

	elif request.user == client.account:
		context = {
			"base_html":	'layout/base.html',
			"sender": 		client,
			"recipient": 	practitioner,
			"conversation":	conversation
		}
		return render(request, "conversations/conversation.html", context)

	return render(request, "test_html/test_failure.html", {"message": "User not authorized"})

def send_message(request):
	# POST-REQUEST TO CREATE MESSAGE FOR CONVERSATION IN DB
	# 
	# for sending messages from Practitioner to TC or CL 
	# AND 
	# for existing CL to send to existing PR
	# 
	# RECIPIENT_CLASS 	(2-CHAR)
	# CONVERSATION_ID 	(CONVERSATION PK)
	# MESSAGE BODY 		(MESSAGE TEXT)
	# 

	if not request.user.is_authenticated:
		return HttpResponseNotFound("User not logged in")

	recipient_class		= request.POST.get("recipient_class")

	conversation_id		= request.POST.get("conversation_id")
	sender 				= request.user
	message				= request.POST.get("message")

	if recipient_class == "TC":
		conversation 		= AnonConversation.objects.get(id=conversation_id)
	else:
		conversation 		= Conversation.objects.get(id=conversation_id)
	
	conversation.send_message(sender, message)

	return JsonResponse({"message":"message received"})


def show_anon_conversation(request):

	# SHOW MESSAGE BETWEEN TC-PR VIA POST (MAY BE CHANGED TO GET)
	# 
	# shows conversation and allows for PR to send message back
	# 
	# RECIPIENT_CLASS 	(2-CHAR)
	# CONVERSATION_ID 	(CONVERSATION PK)
	# MESSAGE BODY 		(MESSAGE TEXT)
	# 

	if not request.user.is_authenticated:
		return HttpResponseNotFound("User not logged in")

	conversation_id		= request.POST.get("conversation_id")
	conversation 		= AnonConversation.objects.get(id=conversation_id)
	
	if int(request.user.practitioner.id) != int(conversation.practitioner.id):
		return HttpResponseNotFound("unauthorized 404")
	else:
		context = {
			"base_html":	'practitioners/base.html',
			"sender": 		conversation.practitioner,
			"recipient":	conversation.temp_client,
			"conversation": conversation,
		}

		return render(request, "conversations/conversation.html", context)

	return HttpResponseNotFound("404")

def send_message_anon(request):
	# POST REQUEST FOR UN-AUTHENTICATED USER TO SEND MESSAGE TO PR
	# 
	# INPUTs:
	# -
	# message 		= message text/body
	# contact_id	= contact id for TC (get_or_create)
	# sender_class 	= "TC"
	# pract_id		= practitioner identifier
	# -
	# if not request.user.is_authenticated:
		# return HttpResponseNotFound("User is logged in")

	temp_client,tcc = Temp_Client.objects.get_or_create(contact_id=request.POST.get("contact_id"))

	practitioner 	= Practitioner.objects.get(id=request.POST.get("pract_id"))
	sender_class	= request.POST.get("sender_class")
	message 		= request.POST.get("message")
	
	if message == "":
		message = "Hello, I am interested in the opportunity to seeing how therapy could help me in my current life."

	conversation,cc = AnonConversation.objects.get_or_create(temp_client=temp_client, practitioner=practitioner)
	conversation.send_message("TC", message)

	# email_message = 'Message sent to ' + practitioner + ', and we will get back to you as soon as possible. Thank you for you, Solace.'

	# send_mail(
	    # 'Solace | Message sent',
	    # email_message,
	    # 'solace.noreply@gmail.com',
	    # [temp_client.contact_id],
	    # fail_silently=False,
	# )

	return render(request, "conversations/message_sent.html", { "user": temp_client})

	