from django.shortcuts import render
from django.http.request import HttpRequest
# from django.views import View
# Create your views here.

def home(request:HttpRequest):
    return render(request, 'core/home.html',{'title':'Home'})

def about(request:HttpRequest):
    return render(request,'core/about.html',{'title':'About'})

def showroom(request:HttpRequest):
    array=[
        'book',
        'this'
    ]
    return render(request,"core/showroom.html",{
        'array':array
    })

def find(request:HttpRequest):
    return render(request,'core/showroom.html',{'title':'Find'})
