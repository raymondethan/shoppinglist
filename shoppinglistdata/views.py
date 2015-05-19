from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import ShoppingItem
from .models import User
from .models import ShoppingList
from .models import ItemList
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
            list = ShoppingList()
            list.list_name = data["username"] + "'s_list"
            list.save()
            response["success"] = "true"
            response["error"] = "None"
    return response

@csrf_exempt
def getlist(request):
    response = HttpResponse()
    if request.method == "GET":
        items = ItemList.objects.filter(str(list_key__list_name=request.GET.get('username')) + "'s_list")
        print(items)
        response["success"] = "true"
        print(request.GET.get('username'))
    #print(username)
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
