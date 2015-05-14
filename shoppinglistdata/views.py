from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import ShoppingItem
import requests
import os
import sys

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)

@csrf_exempt
def newitem(request):
    output = 'sup'
    print("received")
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
        print(output)
        sys.stdout.flush()
        #item = ShoppingItem(request.POST[0])
        #item.save()
        #return render(request, 'newitem.html', {'post': item})
    sys.stdout.flush()
    return HttpResponse(output)

# logging helper
def p(*args):
    print args[0] % (len(args) > 1 and args[1:] or [])
    sys.stdout.flush()

#def db(request):
    
    #greeting = ShoppingItem("eggs")
    #greeting.save()
    
    #greetings = ShoppingItem.objects.all()
    
    #return render(request, 'db.html', {'greetings': greetings})
    #return render(request, 'db.html', {'data': greeting})
