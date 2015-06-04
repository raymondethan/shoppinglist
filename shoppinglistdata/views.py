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
        json_data = json.loads(request.body)
        item = ShoppingItem()
        item.item_name = json_data['item']
        item.save()
        itemlist = ItemList()
        itemlist.item_key = item
        itemlist.user_key = User.objects.filter(username=json_data['username'])[0]
        itemlist.list_key = ShoppingList.objects.filter(list_name=json_data['listname'])[0]
        itemlist.save()
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
        items = ItemList.objects.filter(user_key__username=request.GET.get('username'))
        list_items = []
        for item in items:
            list_items.append(item.item_key.item_name)
        data = {"items": list_items}
        response["success"] = "true"
        response["items"] = json.dumps(data)
    return response

@csrf_exempt
def login(request):
    response = HttpResponse()
    if request.method == "GET":
        if User.objects.filter(username = request.GET.get("username")).count() > 0 and User.objects.filter(username = request.GET.get("username"))[0].password == request.GET.get("password"):
            response["valid"] = "true"
            items = ItemList.objects.filter(user_key__username=request.GET.get('username'))
            list_items = []
            for item in items:
                list_items.append(item.item_key.item_name)
            data = {"items": list_items}
            response["success"] = "true"
            response["items"] = json.dumps(data)
        else:
            response["valid"] = "false"
    return response

@csrf_exempt
def updatecompleted(request):
    response = HttpResponse()
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.filter(username = data["username"])[0]
        for item in data["items"]:
            print(item)
            try:
                i = ItemList.objects.filter(item_key__item_name=item, user_key=user)#, list_key__list_name=user.username+"'_list"
            except:
                print("failed")
            if len(i) == 1:
                i[0].completed = True
                i[0].save()
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
