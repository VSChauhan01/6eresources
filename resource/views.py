from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.

@api_view(['GET', 'POST'])
def data(request):
    if request.method == "POST":
        data = dht.objects.all()
        print("vishal")
        print(data)
        return HttpResponse(data)
    elif request.method == "GET":
        data = dht.objects.all()
        dh={d.temp for d in data}
        print(dh)
        return HttpResponse(dh)

    