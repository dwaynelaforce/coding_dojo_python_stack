from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('user_guess', views.user_guess),
	path('correct', views.correct),
	path('play_again', views.play_again),
]