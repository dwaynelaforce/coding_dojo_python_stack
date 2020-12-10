from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('authors', views.authors),
    path('books/<int:book_id>', views.book_view),
    path('authors/<int:author_id>', views.author_view),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('apply_author', views.apply_author),
    path('apply_book', views.apply_book),
]