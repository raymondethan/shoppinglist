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
    output = 'sup'
    if request.method == 'POST':
        try:
            output = str(request.POST[0])
            output += " post"
        except:
            output = "sup"
        try:
            output = str(request.read())
            output += " read"
        except:
            output = "sub"
        try:
            output = str(request.body)
            output += " body"
        except:
            output = "sup"
        #item = ShoppingItem(request.POST[0])
        #item.save()
        #return render(request, 'newitem.html', {'post': item})
    return HttpResponse(output)


#def db(request):
    
    #greeting = ShoppingItem("eggs")
    #greeting.save()
    
    #greetings = ShoppingItem.objects.all()
    
    #return render(request, 'db.html', {'greetings': greetings})
    #return render(request, 'db.html', {'data': greeting})
