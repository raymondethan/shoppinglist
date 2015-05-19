from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import ShoppingItem
from .models import User
import requests
import os
import sys

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)

@csrf_exempt
def newitem(request):
    response = HttpResponse()
    if request.method == 'POST':
        json_data = json.loads(request.body)['item']
        item = ShoppingItem()
        item.item_name = json_data
        item.save()
    return response

@csrf_exempt
def newuser(request):
    response = HttpResponse()
    if request.method == 'POST':
        data = json.loads(request.body)
        if User.objects.filter(username = data["username"]).count() > 0:
            response["success"] = "false"
            response["error"] = "Username already exists"
        else:
            user = User()
            user.username = data["username"]
            user.password = data["password"]
            user.save()
            response["success"] = "true"
            response["error"] = "None"
    return response

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
