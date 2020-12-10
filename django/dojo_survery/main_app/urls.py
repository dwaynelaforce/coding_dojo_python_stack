from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('form_submit', views.form_submit),
    path('success/<user_name>/<dojo_location>/<fav_lang>/<comment>', views.success),
]