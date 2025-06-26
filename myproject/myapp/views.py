from django.http import HttpResponse, request
from django.shortcuts import render


# Create your Testview here.

def index(request) :
    return render(request, 'index.html')

def dataRender(request) :
    return HttpResponse("Another respons")


def htmlpage(request):
    return render(request,'index.html')