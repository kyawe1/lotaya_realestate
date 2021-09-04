from django.shortcuts import render
from django.http.request import HttpRequest
# Create your views here.

def home(request:HttpRequest):
    return render(request, 'core/home.html')