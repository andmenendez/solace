from django.urls import path

from . import views

# client urls
urlpatterns = [
	path('practitioners/', views.index, name="practitioners_index")
]
