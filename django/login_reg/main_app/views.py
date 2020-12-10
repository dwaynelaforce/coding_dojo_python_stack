from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def register(request):
    errors = User.objects.registration_validator(request.POST)
    if errors:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/')
    if User.objects.filter(email=request.POST['email']):
        messages.error(request, "A user with that email already exists")
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        
        user = User.objects.create(
            fname = request.POST['fname'],
            lname = request.POST['lname'],
            email = request.POST['email'],
            password = hashed_pw
        )
        if 'user_id' not in request.session:
            request.session['user_id'] = user.id
        return redirect('/success')


def login(request):
    errors = User.objects.login_validator(request.POST)
    if not errors:
        user_get = User.objects.filter(email=request.POST['email'])
        if user_get:
            user = user_get.first()
            # if user.password == request.POST['password']:
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/success')
    messages.error(request, "Login failed - check your email or password")
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id = request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/')