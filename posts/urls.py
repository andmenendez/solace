from django.urls import path

from . import views

# client urls
urlpatterns = [
	path('', views.home, name="home"),
	path('ask', views.ask, name="ask"),
	path('list', views.show_anon_post_list, name="show_anon_post_list"),
	path('show/<int:post_id>/', views.show_anon_post, name="show_anon_post"),
]

urlpatterns += [ 
	path('anon_request', views.anon_request, name="anon_request")
]