from django.urls import path

from . import views

# urls

# app_name = 'practitioners'

urlpatterns = [
	path('', views.practitioner_index, name="practitioner_index"),
	path('login', views.practitioner_login, name="practitioner_login"),
	path('register', views.practitioner_register, name="practitioner_register"),
	path('logout', views.practitioner_logout, name="practitioner_logout")
]

urlpatterns += [
	path('practitioner/<int:pract_id>', views.practitioner_public_profile, name="practitioner_public_profile")
]