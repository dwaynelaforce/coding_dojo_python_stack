from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('add_book_review', views.add_book_review),
	path('add_book_review_process', views.add_book_review_process),
	path('book/<int:book_id>', views.book_info),
]