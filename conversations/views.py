from django.shortcuts 		import render
from django.http 			import HttpResponseNotFound

from practitioners.models 	import Practitioner
from clients.models 		import Client
from .models 				import Conversation

from .models import *

# Create your views here.
def client_send_message(request):
	if not request.user.is_authenticated:
		return HttpResponseNotFound("User not logged in")

	Conversation.message_or_create(request)

	context = {"message": "client > opp > post > conversations > message succesfully sent"}

	return render(request, "test_html/test_success.html", context)

def show_conv(request, pk):
	convo 			= Conversation.objects.get(pk = pk)
	client 			= convo.client
	practitioner 	= convo.practitioner

	if request.user == practitioner.account:
		return render(request, "test_html/test_success.html", {"message": convo})
	elif request.user == client.account:
		return render(request, "test_html/test_success.html", {"message": convo})

	return render(request, "test_html/test_failure.html", {"message": convo})