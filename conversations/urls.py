from django.urls import path

from . import views

# urls

urlpatterns = [
	path('', views.client_send_message, name="client_send_message"),
	path('show/<int:pk>', views.show_conv, name="show_conv"),
]