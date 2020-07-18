from django.urls import path

from . import views

# client urls
urlpatterns = [
	path('login', views.client_login, name="client_login"),
	path('register', views.client_register, name="client_register"),
	path('logout', views.client_logout, name="client_logout")
]
