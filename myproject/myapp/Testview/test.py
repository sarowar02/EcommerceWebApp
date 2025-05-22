from django.http import HttpResponse, request
from django.shortcuts import render

# Create your Testview here.

def index(request) :
    return HttpResponse("Hello world,you are at the polls index")

def dataRender(request) :
    return HttpResponse("Another respons")


def htmlpage():
    return render(request,'index.html')