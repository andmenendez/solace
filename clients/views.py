
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, password_validation
from django.core.exceptions import ValidationError

from .forms import AnonForm, ClientInfoForm, ClientLoginForm
from .models import A_post, Temp_Client, Client

# Create your views here.
def index(request):
	if request.method == "POST":
		form = AnonForm(request.POST)
		if form.is_valid():
			return render(request, "test_html/test_success.html", {"message": "client > index > anonform > valid post"})
	else:
		form = AnonForm()
		context= {
			"post_url": "anon_request",
			"controller_name": "Client Index/AnonForm",
			"form": form
		}
	return render(request, "test_html/test_form.html", context)

def anon_request(request):

	title 		= request.POST.get("title")
	body 		= request.POST.get("body")
	contact_id 	= request.POST.get("contact_id")
	is_public 	= request.POST.get("is_public")

	try: 
		a_post = A_post.objects.create(title=title, body=body)
		a_post.save()

		temp_client =Temp_Client.objects.create(contact_id=contact_id, post=a_post)
		temp_client.save()
		
	except ValidationError: 
		return render(request, "test_html/test_failure.html", {"message": "client > anon_request > validation ERROR anon post (NON-PUBLIC)"})
	return render(request, "test_html/test_success.html", {"message": "client > anon_request > successful anon post:: {is_public}"})


def client_register(request):
	form = ClientInfoForm()
	context= {	

		"post_url": "",
		"controller_name": "Client Register",
		"form": form
	}

	return render(request, "test_html/test_form.html", context)

def client_login(request):
	form = ClientLoginForm()
	context= {
		"post_url": "",
		"controller_name": "Client Login",
		"form": form
	}
	return render(request, "test_html/test_form.html", context)
