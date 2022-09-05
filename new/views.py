from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'home.html')

def about(request):
    return HttpResponse("hello this is about page")

def contact(request):
    return HttpResponse("hello this is contack page")
