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
    if request.method == 'POST':
        json_data = json.loads(request.body)['item']
        print("data: " + str(json_data))
        sys.stdout.flush()
        item = ShoppingItem()
        item.item_name = json_data
        print(item)
        sys.stdout.flush()
        item.save()
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
