from core.models import Product
from django.shortcuts import render
from django.http.request import HttpRequest
# from django.views import View
# Create your views here.

def home(request:HttpRequest):
    # a=request.FILES
    return render(request, 'core/home.html',{'title':'Home'})
    # print(request.GET)
    # print(type(request.POST.get('sample')))
    
    # print(request.FILES)
    # for i , j in request.FILES.items():
    #     print(i)
    #     with open('static/core/img/og.jpg', 'wb+' ) as ok:
    #         ok.write(j.read())

def about(request:HttpRequest):
    return render(request,'core/about.html',{'title':'About'})

def showroom(request:HttpRequest):
    array=Product.objects.all()
    temp=[]
    if request.user.is_authenticated:
        o=request.user.interested.all()
        for i in o:
            temp.append(i.product)
    return render(request,"core/showroom.html",{
        'array':array,
        'interested_list':temp
    })

def find(request:HttpRequest):
    array=[]
    if request.GET.get('type'):
        needle=request.GET.get('type')
        array=Product.objects.filter(type=needle)
    elif request.GET.get('any'):
        needle=request.GET.get('any')
        array=Product.objects.filter(name=needle)
    elif request.GET.get('sale_type'):
        needle=request.GET.get('sale_type') 
        array=Product.objects.filter(sale_type=needle) 
    return render(request,'core/showroom.html',{'title':'Find','array':array})

def detail(request:HttpRequest,slug:str):
    o=Product.objects.get(name=slug)
    temp=False
    if (request.user.is_authenticated):
        temp=o.is_interested(request.user)
        more_interest = Product.objects.filter(type=o.type)
        if (len(more_interest)>3):
            more_interest=more_interest[0:3]
    return render(request,'core/detail.html',{
        'obj':o,
        'array':more_interest,
        'is_interested':temp
    })