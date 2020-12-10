from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, 'index.html', context)

def add_user(request):
    user_first_name = request.POST['first_name']
    user_last_name = request.POST['last_name']
    user_email = request.POST['email_address']
    user_age = int(request.POST['age'])
    User.objects.create(first_name=user_first_name, last_name=user_last_name, email_address=user_email, age=user_age)
    return redirect('/')