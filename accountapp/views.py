from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_wolrd(requests):
    return HttpResponse('Hello World!')