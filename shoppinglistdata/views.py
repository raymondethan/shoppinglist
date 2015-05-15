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
    response = {"success": True}
    if request.method == 'POST':
        json_data = json.loads(request.body)['item']
        item = ShoppingItem()
        item.item_name = json_data
        item.save()
    return HttpResponse(response)

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
