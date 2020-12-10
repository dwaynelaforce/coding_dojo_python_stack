from django.db import models
from login_reg_app.models import User
from datetime import date, datetime

# Create your models here.

class TripManager(models.Manager):
    def trip_validator(self, postdata):
        errors = {}
        if len(postdata['destination']) < 3:
            errors['destination'] = "Destination must be at least 3 characters"
        if len(postdata['plan']) < 3:
            errors['plan'] = "Plan must be at least 3 characters"
        if not postdata['start_date']:
            errors['start_date'] = "Start date cannot be empty"
        if not postdata['end_date']:
            errors['end_date'] = "End date cannot be empty"

        # black belt validations
        start_date = datetime.strptime(postdata['start_date'], "%Y-%m-%d")
        end_date = datetime.strptime(postdata['end_date'], "%Y-%m-%d")
        if start_date <= datetime.today():
            errors['start_date_past'] = "Start date cannot be in the past"
        if start_date > end_date:
            errors['end_before_start'] = "End date cannot be before start date (time travel impossible, sorry)"

        print("##################### debugging ########################")
        print(errors)
        print("##################### debugging ########################")

        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=55)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.CharField(max_length=255)
    created_by_user = models.ForeignKey(User, related_name="trips_created", on_delete=models.CASCADE)
    joined_by_users = models.ManyToManyField(User, related_name="trips_joined")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
