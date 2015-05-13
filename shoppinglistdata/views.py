from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import ShoppingItem
import requests
import os

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)

@csrf_exempt
def newitem(request):
    file = open("request.txt", "w")
    file.write(request.method)
    file.write(request.body)
    if request.method == 'POST':
        json_data = request.body
        #json_data = json.decode(request.GET())
        file.write("post")
    else:
        file.write(request.body)
    file.close()
    return HttpResponse("hello")


#def db(request):
    
    #greeting = ShoppingItem("eggs")
    #greeting.save()
    
    #greetings = ShoppingItem.objects.all()
    
    #return render(request, 'db.html', {'greetings': greetings})
    #return render(request, 'db.html', {'data': greeting})
