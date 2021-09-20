from django.http import response
from django.shortcuts import redirect, render
from core.models import Notified, Product
from .helper import validate,check_fake_admin
from django.core.files.images import ImageFile
from django.core.files import File
from realestate import settings
import os
from django.contrib.auth import  get_user_model

# Create your views here.
@check_fake_admin
def create_house(request):
    if request.method == "POST":
        arr = [
            "name",
            "type",
            "number_of_rooms",
            "number_of_bathrooms",
            "funiture_ready",
            "address",
            "price",
            "sale_type",
        ]
        temp = validate(arr, request.POST)
        if temp:
            temp["funiture_ready"] = True if temp["funiture_ready"] == "Y" else False
            k = Product.objects.create(**temp)
            f=File(request.FILES.get('coverphoto'))
            p=os.path.join('coverphoto.jpg')
            # k.set_slug()
            k.coverphoto.save(p,f,save=False)
            k.save()
    return render(request, "fake_admin/create_house.html")
@check_fake_admin
def list_house(request):
    m=Product.objects.all()
    return render(request,'fake_admin/list_house.html',{'array':m})

@check_fake_admin
def freeze_user(request,uid:int):
    if request.method == "POST":
        user=get_user_model()
        obj=user.objects.get(id=uid)
        obj.is_active=False
        obj.save()
        return response.JsonResponse("success",safe=False)

@check_fake_admin
def list_user(request):
    user=get_user_model()
    n=user.objects.filter(is_superuser=False)
    if not n:
        n= False
    return render(request,'fake_admin/list_user.html',{'array':n})

@check_fake_admin
def delete_user(request,uid:int):
    if request.method == "POST":
        user=get_user_model()
        obj=user.objects.get(id=uid)
        obj.delete()

@check_fake_admin
def notification_list(request):
    notified=Notified.objects.all()
    return render(request,'list_notify.html',{'array':notified})
