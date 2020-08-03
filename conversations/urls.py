from django.urls import path

from . import views

# urls

urlpatterns = [
	path('', views.send_message, name="send_message"),
	path('show/c', views.show_conversation, name="show_conversation"),
	path('show/a', views.show_anon_conversation, name="show_anon_conversation"),
	# path('start_conversation', views.start_conversation, name="start_conversation"),
]

urlpatterns += [
	path('conversation/send_message', views.send_message, name="send_message"),
	path('conversation/send_message_anon/', views.send_message_anon, name="send_message_anon")
]