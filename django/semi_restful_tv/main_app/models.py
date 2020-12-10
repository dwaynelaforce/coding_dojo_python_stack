from django.db import models
from datetime import date

class ShowManager(models.Manager):
    def validator(self, postdata):
        rel_date = date.fromisoformat(postdata['release_date'])
        errors = {}
        if len(postdata['title']) < 2:
            errors['title'] = "Title must be at least 2 characters"
        if len(postdata['network']) < 3:
            errors['network'] = "Network must be at least 3 characters"
        if len(postdata['desc']) < 10 and len(postdata['desc']) != 0:
            errors['desc'] = "Description must be at least 10 characters or left blank"
        if rel_date > date.today():
            errors['release_date'] = "Release date must be today or before"
        return errors

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=55)
    network = models.CharField(max_length=55)
    release_date = models.DateField(blank=True)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()