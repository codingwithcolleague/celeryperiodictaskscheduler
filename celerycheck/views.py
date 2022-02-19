from django.http import HttpResponse
from django.shortcuts import render
from .task import add
# Create your views here.


def check(request):
    add.delay(10,20)
    return HttpResponse("Hello How are you ?")