from django.http import HttpResponse, request
from django.shortcuts import render

def index(request):
    return render(request,'index.html')