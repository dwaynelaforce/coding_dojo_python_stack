from django.urls import path
from . import views

urlpatterns = [
	path('', views.fav_books_home),
    path('add_book', views.add_book),
    path('view_book/<int:book_id>', views.view_book),
    path('unfavorite/<int:book_id>', views.unfavorite),
    path('add_book_to_favs/<int:book_id>', views.add_book_to_favs),
    path('delete/<int:book_id>', views.delete_book),
    path('edit/<int:book_id>', views.edit_book),
    path('edit/<int:book_id>/process', views.edit_book_process),
]