from django.shortcuts 			import render

from django.contrib.auth 		import authenticate, login, logout, password_validation
from django.core.exceptions 	import ValidationError
from django.http 				import HttpResponseRedirect
from django.urls 				import reverse

from .models 					import Practitioner
from .forms 					import PractInfoForm, PractLoginForm
from conversations.models 		import Conversation, Message
from clients.models				import Client
from posts.models 				import Anon_Post
from django.contrib.auth.models import User

# Create your views here.
def practitioner_index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('practitioner_login'))
	# try: 
	context = {
		"conv_list":Conversation.objects.filter(practitioner=request.user.practitioner),
		"post_list":Anon_Post.objects.all()
	}
	return render(request, "practitioners/index.html", context)
	
	# except:
	# 	return render(request, "test_html/test_failure.html", {"message": "not practitioner"})

# PRACTITIONER ACCOUNTS \\ LOGIN, REGISTRATION, VIEWS
def practitioner_login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse("practitioner_index"))
	if request.method == "GET":
		context= {
			"post_url": "practitioner_login",
			"controller_name": "Practitioner Login",
			"form": PractLoginForm()
		}
		return render(request, "practitioners/form.html", context)

	username = request.POST.get("username")
	password = request.POST.get("password")
	
	user = authenticate(request, username=username, password=password)

	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("practitioner_index"))

	else:
		return render(request, "test_html/test_failure.html", {"message": "client_login > POST > user login failed"})


def practitioner_register(request):
	if request.method=="GET":
		form = PractInfoForm()
		context= {	
			"post_url": "practitioner_register",
			"controller_name": "Practitioner Register",
			"form": form
		}
		return render(request, "practitioners/form.html", context)
	
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

def practitioner_public_profile(request, pract_id):
	context = {
		"pract": Practitioner.objects.get(id = pract_id)
	}
	return render(request, "practitioners/practitioner_public_profile.html", context)