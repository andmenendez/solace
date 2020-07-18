from django.urls import path

from . import views

# client urls
urlpatterns = [
	path('', views.practitioner_index, name="practitioner_index"),
	path('login', views.practitioner_login, name="practitioner_login"),
	path('register', views.practitioner_register, name="practitioner_register"),
	path('logout', views.practitioner_logout, name="practitioner_logout")
]
