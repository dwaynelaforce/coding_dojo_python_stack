from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('shows', views.shows),
	path('shows/<int:show_id>', views.show_info),
	path('shows/new', views.new_show),
	path('process_new_show', views.process_new_show),
	path('shows/<int:show_id>/edit', views.edit_show),
	path('shows/<int:show_id>/edit/process', views.edit_process),
	path('shows/<int:show_id>/delete', views.delete_show),
]