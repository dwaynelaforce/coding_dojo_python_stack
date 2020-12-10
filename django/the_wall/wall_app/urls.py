from django.urls import path
from . import views

urlpatterns = [
	path('', views.wall),
    path('/post_msg', views.post_msg),
    path('/<int:post_id>/delete', views.delete),
    path('/<int:post_id>/comments', views.comments),
    path('/<int:post_id>/post_comment', views.post_comment),
    path('/<int:post_id>/comments/<int:comment_id>/delete', views.delete_comment),
]