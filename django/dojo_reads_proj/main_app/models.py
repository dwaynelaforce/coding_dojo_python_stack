from django.db import models
from login_reg_app.models import User
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=55)

class Book(models.Model):
    title = models.CharField(max_length=55)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)


class Review(models.Model):
    rating = models.IntegerField()
    desc = models.CharField(max_length=511)
    user = models.ForeignKey(User, related_name="reviews_written", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="book_reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)