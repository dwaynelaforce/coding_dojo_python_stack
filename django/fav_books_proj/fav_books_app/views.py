from django.shortcuts import render, redirect
from django.contrib import messages
from login_reg_app.models import User
from .models import Book

# Create your views here.
def fav_books_home(request):
    if 'user_id' not in request.session:
        return redirect('/')
    request.session['user_loc'] = "home"
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'books': Book.objects.all().order_by("-created_at")
    }
    return render(request, 'fav_books_home.html', context)

def add_book(request):
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Book.objects.book_validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect ('/fav_books')
    this_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
        created_by_user = this_user
    )
    this_book.liked_by_users.add(this_user)
    return redirect(f'/fav_books/view_book/{this_book.id}')

def view_book(request, book_id):
    if 'user_id' not in request.session or 'user_loc' not in request.session:
        return redirect('/')
    request.session['user_loc'] = "book"
    this_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.get(id=book_id)
    these_users = this_book.liked_by_users.all()
    context = {
        'user': this_user,
        'book': this_book
    }
    return render(request, 'view_book.html', context)

def unfavorite(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.get(id=book_id)
    if this_user not in this_book.liked_by_users.all():
        return redirect(f'/fav_books/view_book/{this_book.id}')
    this_user.books_liked.remove(this_book)
    if request.session['user_loc'] == "book":
        return redirect(f'/fav_books/view_book/{book_id}')
    return redirect('/fav_books')

def add_book_to_favs(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.get(id=book_id)
    if this_user in this_book.liked_by_users.all():
        return redirect(f'/fav_books/view_book/{book_id}')
    this_user.books_liked.add(this_book)
    if request.session['user_loc'] == "book":
        return redirect(f'/fav_books/view_book/{book_id}')
    return redirect('/fav_books')

def delete_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.get(id=book_id)
    if this_user != this_book.created_by_user:
        return redirect('/fav_books')
    this_book.delete()
    return redirect('/fav_books')

def edit_book(request, book_id):
    if 'user_id' not in request.session or 'user_loc' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.get(id=book_id)
    if this_user != this_book.created_by_user:
        return redirect('/fav_books')
    context = {
        'book': this_book
    }
    return render(request, 'edit_book.html', context)

def edit_book_process(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Book.objects.book_validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect (f'/fav_books/edit/{book_id}')
    this_user = User.objects.get(id=request.session['user_id'])
    this_book = Book.objects.get(id=book_id)
    if this_user != this_book.created_by_user:
        return redirect(f'/fav_books/view_book/{book_id}')
    this_book.title = request.POST['title']
    this_book.desc = request.POST['desc']
    this_book.save()
    return redirect(f'/fav_books/view_book/{book_id}')


