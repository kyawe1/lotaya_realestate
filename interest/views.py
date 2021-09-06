from django.shortcuts import render
from django.http.request import HttpRequest
# Create your views here.

def interest(request:HttpRequest):
    return render(request,"interest/list.html",{'list':'Interested'})

