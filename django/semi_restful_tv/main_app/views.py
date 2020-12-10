from django.shortcuts import render, HttpResponse, redirect
from main_app.models import *
from datetime import date
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'tv_shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def show_info(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'show_info.html', context)

def edit_show(request, show_id):
    my_show = Show.objects.get(id=show_id)
    rel_date = my_show.release_date.strftime("%Y-%m-%d")
    context = {
        'show': Show.objects.get(id=show_id),
        'release_date': rel_date
    }
    return render(request, 'edit_show.html', context)

def edit_process(request, show_id):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        print(errors)
        return redirect(f'/shows/{show_id}/edit')
    my_show = Show.objects.get(id = show_id)
    my_show.title = request.POST['title']
    my_show.network = request.POST['network']
    my_show.release_date = date.fromisoformat(request.POST['release_date'])
    my_show.desc = request.POST['desc']
    my_show.save()
    return redirect(f'/shows/{show_id}')

def delete_show(request, show_id):
    my_show = Show.objects.get(id = show_id)
    my_show.delete()
    return redirect('/shows')



def new_show(request):
    return render(request, 'new_show.html')

def process_new_show(request):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        print(errors)
        return redirect(f'/shows/new')
    my_show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = date.fromisoformat(request.POST['release_date']),
        desc = request.POST['desc']
    )
    return redirect(f'/shows/{my_show.id}')

