from django import http
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    if 'visit_count' in request.session:
        count = request.session['visit_count']
        count += 1
        request.session['visit_count'] = count
    else:
        request.session['visit_count'] = 1
    print("visit_count: ", request.session['visit_count'])
    return render(request, 'index.html')

def destroy(request):
    del request.session['visit_count']
    print("visit_count has been DESTROYED")
    return redirect('/')

def plustwo(request):
    count = request.session['visit_count']
    count += 1
    request.session['visit_count'] = count
    return redirect('/')

def increment(request):
    number = int(request.POST['number']) - 1
    count = request.session['visit_count']
    count += number
    request.session['visit_count'] = count
    return redirect('/')
