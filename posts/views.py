from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Anon_Post, Temp_Client
from .forms import AnonForm
from django.core.exceptions import ValidationError


# Create your views here.
def index(request):
	if request.method == "POST":
		form = AnonForm(request.POST)
		context = {"message": "client > index > anonform > valid post"}
		if form.is_valid():
			return render(request, "test_html/test_success.html", context)
	else:
		form = AnonForm()
		context = {
			"post_url": "anon_request",
			"controller_name": "Client Index/AnonForm",
			"form": form
		}
	return render(request, "anon_request/index.html", context)



# TEMP CLIENTS \\ INDEX/HOME VIEW, POST AND FORMS
def anon_request(request):

	title 		= "test [remove title column]"
	body 		= request.POST.get("body")
	contact_id 	= request.POST.get("contact_id")

	try: 
		anon_post = Anon_Post.objects.create(title=title, body=body)
		anon_post.save()

		temp_client =Temp_Client.objects.create(contact_id=contact_id, post=anon_post)
		temp_client.save()

	except ValidationError: 
		return render(request, "test_html/test_failure.html", {"message": "client > anon_request > validation ERROR anon post (NON-PUBLIC)"})

	return HttpResponseRedirect(reverse("show_anon_post_list"))

def show_anon_post_list(request):
	context = {
		"post_list": Anon_Post.objects.all()
	}
	return render(request, "anon_request/show_anon_post_list.html", context)

def show_anon_post(request, post_id):
	context = {
		"post": Anon_Post.objects.get(pk = post_id)
	}
	return render(request, "anon_request/show_anon_post.html", context)
