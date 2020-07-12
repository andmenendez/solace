from django.urls import path

from . import views

# client urls
urlpatterns = [
	path('', views.index, name="home"),
	path('login', views.client_login, name="client_login"),
	path('register', views.client_register, name="client_registration")
]

urlpatterns += [ 
	path('anon_request', views.anon_request, name="anon_request")
]
