from django.urls import path

from . import views

# client urls
urlpatterns = [
	path('posts', views.index, name="posts")
]
