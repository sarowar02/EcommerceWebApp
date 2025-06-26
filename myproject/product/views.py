from itertools import product

from django.shortcuts import render
import templates

# Create your views here.
def home2(request):
    return render(request,'home2.html')

def index(request):
    return render(request, 'list.html')