from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home(request):
    context = {
        'all_reviews': Review.objects.all(),
    }
    return render(request, 'home.html', context)

def add_book_review(request):
    return render(request, 'add_book_review.html')

def add_book_review_process(request):
    if request.POST['new_author']:
        this_author = Author.objects.create(name=request.POST['new_author'])
    else:
        this_author = request.POST['author']
    this_book = Book.objects.create(
        title = request.POST['title'],
        author = this_author
    )
    this_review = Review.objects.create(
        rating = int(request.POST['rating']),
        desc = request.POST['desc'],
        user = User.objects.get(id=request.session['user_id']),
        book = this_book
    )
    print(this_review.__dict__)
    return redirect(f'/dojo_reads/book/{this_book.id}')

def book_info(request, book_id):
    this_book = Book.objects.get(id=book_id)
    context = {
        'book': this_book
    }
    return render(request, 'book_info.html', context)