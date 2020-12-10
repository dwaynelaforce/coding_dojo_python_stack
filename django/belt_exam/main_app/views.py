from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from datetime import date, datetime

# Create your views here.
def home(request):
    this_user = User.objects.get(id=request.session['user_id'])
    unjoined_trips = []
    for trip in Trip.objects.all():
        if this_user not in trip.joined_by_users.all():
            unjoined_trips.append(trip)
    
    context = {
        'user': this_user,
        'user_trips': this_user.trips_joined.all().order_by("-created_at"),
        'unjoined_trips': unjoined_trips
    }
    return render(request, 'home.html', context)

def create_trip(request):
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': this_user
    }
    return render(request, 'create_trip.html', context)

def create_trip_process(request):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/home/create_trip')
    this_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.create(
        destination = request.POST['destination'],
        start_date = datetime.strptime(request.POST['start_date'], "%Y-%m-%d"),
        end_date = datetime.strptime(request.POST['end_date'], "%Y-%m-%d"),
        plan = request.POST['plan'],
        created_by_user = this_user
    )
    this_trip.joined_by_users.add(this_user)
    return redirect('/home')

def trip_info(request, trip_id):
    this_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=trip_id)

    #black belt people who've joined the trip minus the trip's creator
    joined_users = []
    for user in this_trip.joined_by_users.all():
        if user != this_trip.created_by_user:
            joined_users.append(user)

    context = {
        'user': this_user,
        'trip': this_trip,
        'joined_users': joined_users
    }
    return render(request, 'trip_info.html', context)

def trip_delete(request, trip_id):
    this_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=trip_id)
    if this_user == this_trip.created_by_user:
        this_trip.delete()
    return redirect('/home')

def trip_edit(request, trip_id):
    this_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=trip_id)
    if this_user != this_trip.created_by_user:
        return redirect(f'/home/trips/{trip_id}')
    
    #black belt for auto-populating date fields
    start_date_string = this_trip.start_date.strftime("%Y-%m-%d")
    end_date_string = this_trip.end_date.strftime("%Y-%m-%d")
    
    
    
    context = {
        'user': this_user,
        'trip': this_trip,
        'start_date': start_date_string,
        'end_date': end_date_string
    }




    return render(request, 'trip_edit.html', context)

def trip_edit_process(request, trip_id):
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect(f'/home/trips/{trip_id}/edit')
    # update trip
    this_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=trip_id)
    
    this_trip.destination = request.POST['destination']
    this_trip.start_date = datetime.strptime(request.POST['start_date'], "%Y-%m-%d")
    this_trip.end_date = datetime.strptime(request.POST['end_date'], "%Y-%m-%d")
    this_trip.plan = request.POST['plan']
    this_trip.save()

    return redirect('/home')

def trip_join(request, trip_id):
    this_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=trip_id)
    this_trip.joined_by_users.add(this_user)
    return redirect('/home')

def trip_un_rsvp(request, trip_id):
    this_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=trip_id)
    this_trip.joined_by_users.remove(this_user)
    return redirect('/home')
