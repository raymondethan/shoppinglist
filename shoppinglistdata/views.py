from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import ShoppingItem
import requests
import os

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)

def newitem(request):
    if request.method == 'POST':
        json_data = request.GET()
        #json_data = json.decode(request.GET())
        print(json_data)
    else:
        print("not a post")
    return HttpResponse("Got it")


#def db(request):
    
    #greeting = ShoppingItem("eggs")
    #greeting.save()
    
    #greetings = ShoppingItem.objects.all()
    
    #return render(request, 'db.html', {'greetings': greetings})
    #return render(request, 'db.html', {'data': greeting})
