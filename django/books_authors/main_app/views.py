from django import http
from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

# ----------------BOOKS------------------

def books(request):
    context = {
        'booklist': Book.objects.all()
    }
    return render(request, 'books.html', context)

def add_book(request):
    book_title = request.POST['title']
    book_desc = request.POST['desc']
    Book.objects.create(title=book_title, desc=book_desc)
    return redirect('/books')

def book_view(request, book_id):
    list = []
    for author in Book.objects.get(id=book_id).authors.all():
        list.append(author.id)
    print(list)
    context = {
        'book_info': Book.objects.get(id=book_id),
        'book_authors': Book.objects.get(id=book_id).authors.all(),
        'avail_authors': Author.objects.exclude(id__in=list)
    }
    return render(request, 'bookview.html', context)

def apply_author(request):
    new_author_id = int(request.POST['new_author'])
    book_id = int(request.POST['book'])
    Book.objects.get(id=book_id).authors.add(new_author_id)
    return redirect(f'books/{book_id}')



# ---------------AUTHORS------------------

def authors(request):
    context = {
        'authorlist': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def add_author(request):
    author_name = request.POST['name']
    author_notes = request.POST['notes']
    Author.objects.create(name=author_name, notes=author_notes)
    return redirect('/authors')

def author_view(request, author_id):
    list = []
    for book in Author.objects.get(id=author_id).books.all():
        list.append(book.id)
    print(list)
    context = {
        'author_info': Author.objects.get(id=author_id),
        'author_books': Author.objects.get(id=author_id).books.all(),
        'avail_books': Book.objects.exclude(id__in=list)
    }
    return render(request, 'authorview.html', context)

def apply_book(request):
    new_book_id = request.POST['new_book']
    author_id = request.POST['author']
    Author.objects.get(id=author_id).books.add(new_book_id)
    return redirect(f'authors/{author_id}')