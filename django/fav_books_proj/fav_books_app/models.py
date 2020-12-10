from django.db import models
from login_reg_app.models import User

# Create your models here.

class BookManager(models.Manager):
    def book_validator(self, postdata):
        errors = {}
        if len(postdata['title']) < 2 or len(postdata['desc']) < 2:
            errors['general'] = "book title and description must be at least 2 characters"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.ForeignKey(User, related_name="books_created", on_delete=models.CASCADE)
    liked_by_users = models.ManyToManyField(User, related_name="books_liked")
    objects = BookManager()