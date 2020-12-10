from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def registration_validator(self, postdata):
        errors = {}
        if len(postdata['name']) < 2:
            errors['name'] = "Name must be at least 2 characters"
        if len(postdata['alias']) < 2:
            errors['alias'] = "Alias must be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "Invalid email address"
        if len(postdata['password']) < 12:
            errors['password'] = "Passwords must be at least 12 characters"
        if postdata['password'] != postdata['confirm_password']:
            errors['confirm_password'] = "Passwords do not match"
        return errors

    def login_validator(self, postdata):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "Invalid email address"
        if len(postdata['password']) < 12:
            errors['password'] = "Passwords must be at least 12 characters"
        return errors

class User(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    objects = UserManager()