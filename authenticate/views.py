from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as django_login,get_user_model,logout as django_logout
from django.http import HttpRequest
from helper import checkloggedin
# Create your views here.

def login(request:HttpRequest):
    if checkloggedin(request):
        if request.method=="POST":
            if request.POST.get('password') and request.POST.get('username'):
                obj=authenticate(request,username=request.POST.get('username'),password=request.POST.get("password"))
                django_login(request,obj)
                nex=request.GET.get('next')
                messages.add_message(request,messages.SUCCESS,"success")
                if nex:
                    return redirect(nex)
                return redirect('core:home')
            messages.add_message(request,messages.ERROR,"Something Wrong")
        return render(request,'authenticate/login.html',{'title':'Login'})
    return redirect('core:home')

def register(request):
    if checkloggedin(request):
        if request.method=='POST':
            if request.POST.get('password')==request.POST.get('repassword') and request.POST.get('passwrod') and request.POST.get('repassword') and request.POST.get('username') and request.POST.get('email'):
                obj=get_user_model()
                m=obj.objects.create(request.POST)
                m.save()
                messages.add_message(request,messages.SUCCESS,"success")
            messages.add_message(request,messages.ERROR,"Something Wrong")
        return render(request,'authenticate/register.html',{'title':'Register'})
    return redirect('core:home')

@login_required
def logout(request):
    django_logout(request)
    return redirect('core:home')