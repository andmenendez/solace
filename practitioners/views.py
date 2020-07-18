from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout, password_validation
from django.core.exceptions import ValidationError

from .models import Practitioner
from .forms import PractInfoForm
from django.contrib.auth.models import User

# Create your views here.
def practitioner_index(request):
	return render(request, "practitioners/index.html")

# PRACTITIONER ACCOUNTS \\ LOGIN, REGISTRATION, VIEWS
def practitioner_login(request):
	if request.method == "GET":
		form = PractInfoForm()
		context= {
			"post_url": "practitioner_login",
			"controller_name": "Practitioner Login",
			"form": form
		}
		return render(request, "test_html/test_form.html", context)

	username = request.POST.get("username")
	password = request.POST.get("password")
	
	user = authenticate(request, username=username, password=password)

	if user is not None:
		login(request, user)
		return render(request, "test_html/test_success.html", {"message": "practitioner_login > POST > user login SUCCESS"})

	else:
		return render(request, "test_html/test_failure.html", {"message": "practitioner_login > POST > user login failed"})


def practitioner_register(request):
	if request.method=="GET":
		form = PractInfoForm()
		context= {	
			"post_url": "practitioner_register",
			"controller_name": "Practitioner Register",
			"form": form
		}
		return render(request, "test_html/test_form.html", context)
	
	form = PractInfoForm(request.POST)

	if form.is_valid():

		username 	= form.cleaned_data.get("username")
		password 	= form.cleaned_data.get("password")
		password_c	= form.cleaned_data.get("password_c")

		if password != password_c:
			return render(request, "test_html/test_failure.html", {"message": "practitioner_register > POST > PRACT PW do not match"})

		user_info = {
			'first_name' 	: form.cleaned_data.get("first_name"),
			'last_name' 	: form.cleaned_data.get("last_name"),
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

			Practitioner.createPractitioner(user, user_info)

			return render(request, "test_html/test_success.html", {"message": "practitioner_register > POST > user registered and logged in SUCCESS"})
		except ValidationError:
			return render(request, "test_html/test_failure.html", {"message": "practitioner_register > POST > practitioner save FAILED"})
	return render(request, "test_html/test_failure.html", {"message": "practitioner_register > POST > user FAILED to register"})


def practitioner_logout(request):
	logout(request)
	return render(request, "test_html/test_success.html", {"message": "practitioner_logout > POST > logout SUCCESS"})
