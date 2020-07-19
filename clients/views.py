

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, password_validation
from django.core.exceptions import ValidationError

from django.http import HttpResponseRedirect
from django.urls import reverse


from .forms import ClientInfoForm, ClientLoginForm
from .models import Client
from django.contrib.auth.models import User

from practitioners.models import Practitioner

# Create your views here.

# CLIENT ACCOUNTS \\ LOGIN, REGISTRATION, VIEWS

def client_login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse("client_profile"))
	if request.method == "GET":
		context= {
			"post_url": "client_login",
			"controller_name": "Client Login",
			"form": ClientLoginForm()
		}
		return render(request, "test_html/test_form.html", context)

	username = request.POST.get("username")
	password = request.POST.get("password")
	
	user = authenticate(request, username=username, password=password)

	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("client_profile"))

	else:
		return render(request, "test_html/test_failure.html", {"message": "client_login > POST > user login failed"})


def client_register(request):
	if request.method=="GET":
		form = ClientInfoForm()
		context= {

			"post_url": "client_register",
			"controller_name": "Client Register",
			"form": form
		}
		return render(request, "test_html/test_form.html", context)
	
	form = ClientInfoForm(request.POST)

	if form.is_valid():

		username 	= form.cleaned_data.get("username")
		password 	= form.cleaned_data.get("password")
		password_c	= form.cleaned_data.get("password_c")

		if password != password_c:
			return render(request, "test_html/test_failure.html", {"message": "client_registration > POST > Client PW do not match"})

		user_info = {
			'first_name' 	: form.cleaned_data.get("first_name"),
			'last_name' 	: form.cleaned_data.get("last_name"),
			'birthday' 		: form.cleaned_data.get("birthday"),
			'email' 		: form.cleaned_data.get("email"),
			'phone' 		: form.cleaned_data.get("phone"),
			'zipcode' 		: form.cleaned_data.get("zipcode")
		}

		try:
			password_validation.validate_password(password)
			user = User.objects.create(username=username)
			user.set_password(password)
			user.save()

			login(request, user)
			user = authenticate(request, username=username, password=password)

			Client.createClient(user, user_info)

			return render(request, "test_html/test_success.html", {"message": "client_registration > POST > user registered and logged in SUCCESS"})
		except ValidationError:
			return render(request, "test_html/test_failure.html", {"message": "client_registration > POST > Client.save() FAILED"})
	return render(request, "test_html/test_failure.html", {"message": "client_registration > POST > user FAILED to register"})

def client_logout(request):
	logout(request)
	return render(request, "test_html/test_success.html", {"message": "client_logout > POST > logout SUCCESS"})


def client_profile(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("client_login"))
	return render(request, "clients/profile.html")

def client_opportunities(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("client_login"))
	context = {
		"practitioners": Practitioner.objects.all()
	}
	return render(request, "clients/opportunities.html", context)
