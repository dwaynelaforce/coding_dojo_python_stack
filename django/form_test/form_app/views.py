from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_user(request):
    print(".....................got POST info......................")
    print(request.POST)
    name_from_user = request.POST['name']
    email_from_user = request.POST['email']
    birthdate_from_user = request.POST['birthdate']
    print(name_from_user, email_from_user)
    context = {
        "name_on_template": name_from_user,
        "email_on_template": email_from_user,
        "birthdate_on_template": birthdate_from_user
    }
    return redirect('/success')

def success(request):
    return render(request, 'success.html')