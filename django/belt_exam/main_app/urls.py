from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('create_trip', views.create_trip),
	path('create_trip/process', views.create_trip_process),
	path('trips/<int:trip_id>', views.trip_info),
	path('trips/<int:trip_id>/delete', views.trip_delete),
	path('trips/<int:trip_id>/edit', views.trip_edit),
	path('trips/<int:trip_id>/edit/process', views.trip_edit_process),
	path('trips/<int:trip_id>/join', views.trip_join),
	path('trips/<int:trip_id>/un_rsvp', views.trip_un_rsvp),
]