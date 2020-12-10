from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        'all_dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    new_dojo_name = request.POST['name']
    new_dojo_city = request.POST['city']
    new_dojo_state = request.POST['state']
    Dojo.objects.create(
        name = new_dojo_name,
        city = new_dojo_city,
        state = new_dojo_state,
        desc = "None"
    )
    return redirect('/')

def add_ninja(request):
    new_ninja_first = request.POST['first_name']
    new_ninja_last = request.POST['last_name']
    new_ninja_dojo = Dojo.objects.get(id=int(request.POST['dojo']))
    Ninja.objects.create(
        dojo_id = new_ninja_dojo,
        first_name = new_ninja_first,
        last_name = new_ninja_last
    )
    return redirect('/')