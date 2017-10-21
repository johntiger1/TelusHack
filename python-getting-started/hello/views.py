from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt

from .models import Greeting
import os
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import CollectionSerializer



# Create your views here.
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + "This is the response served, new push in."
                                  "Welcome to the app!" +
                        r.text + '</pre>')
    # return HttpResponse('Hello from Python!')
    # return render(request, 'index.html')
@csrf_exempt
def extrapage(request):
    context = {'my_var': "default1"}
    if request.method == "GET":
        context = {'my_var': "GET"}
        # return render(request, "extrapage.html")
    elif request.method == "POST":
        context = {'my_var': "POST"}

    return render(request, "extrapage.html", context=context)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

# now, set up the routes to take in data from a json


class CollectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = CollectionSerializer
