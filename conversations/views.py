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

	if not request.user.is_authenticated:
		return HttpResponseNotFound("User not logged in")

	conversation_id	= request.POST.get("conversation_id")
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
	# if not request.user.is_authenticated:
		# return HttpResponseNotFound("User not logged in")

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
	# if not request.user.is_authenticated:
	return HttpResponseNotFound("User is logged in")

# 	practitioner 	= Practitioner.objects.get(id=request.POST.get("pract_id"))
# 	temp_client,ctc = Temp_Client.objects.get_or_create(contact_id=request.POST.get("contact_id"))
# 	sender_class	= request.POST.get("sender_class")
# 	message 		= request.POST.get("message")
	
# 	if message == "":
# 		message = "Hello"

# 	a_conversation,cc = AnonConversation.objects.get_or_create(temp_client=temp_client, practitioner=practitioner)
# 	a_conversation.send_message("TC", message)

# 	if sender_class == "TC":
# 		# IF MESSAGE FROM TC
# 		return render(request, "conversations/message_sent.html")
# 	# IF MESSAGE FROM PR
# 	return JsonResponse({"message":"PR message sent and received"})



	