from django.shortcuts import render, HttpResponse, redirect
import random
from time import localtime

# Create your views here.
def index(request):
    if 'purse' not in request.session:
        request.session['purse'] = 0
    return render(request, 'index.html')

def process_money(request):
    if 'log' not in request.session:
        request.session['log'] = []
    if request.POST['choice'] == "farm":
        earnings = random.randint(10, 20)
        log = f"worked on farm, earned {earnings} gold"
    elif request.POST['choice'] == "cave":
        earnings = random.randint(5, 10)
        log = f"went to cave, earned {earnings} gold"
    elif request.POST['choice'] == "house":
        earnings = random.randint(2, 5)
        log = f"worked at house, earned {earnings} gold"
    else:            # choice == casino
        coinflip = random.randint(1, 2)
        if coinflip == 1:
            earnings = 50
            log = "won 50 gp at the casino"
        else:
            earnings = -50
            log = "lost 50 gp at the casino"
    request.session['purse'] += earnings
    request.session['log'].append(log)
    
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')