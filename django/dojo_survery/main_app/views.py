from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form_submit(request):
    user_name = request.POST['user_name']
    dojo_location = request.POST['dojo_location']
    fav_lang = request.POST['fav_lang']
    comment = request.POST['comment']
    return redirect(f"/success/{user_name}/{dojo_location}/{fav_lang}/{comment}")

def success(request, user_name, dojo_location,fav_lang,comment):
    context = {
        'user_name': user_name,
        'dojo_location': dojo_location,
        'fav_lang': fav_lang,
        'comment': comment
    }
    return render(request, 'success.html', context)