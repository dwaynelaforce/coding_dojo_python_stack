from django.shortcuts import render, redirect, HttpResponse
from time import time, gmtime, strftime, localtime

# Create your views here.
def root(request):
    context = {
        'date': strftime("%A, %B %d", localtime()),
        'time': strftime("%X", localtime())
    }
        
    
    return render(request,'index.html', context)