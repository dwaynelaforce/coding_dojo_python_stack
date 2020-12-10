from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        "name": "Dwayne",
        "favorite_color": "purple",
        "pets": ["oscar","river","bear"]
    }
    return render(request, "index.html", context)

def blogs(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("this is a placeholder to create a new blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
    return redirect('/blogs')