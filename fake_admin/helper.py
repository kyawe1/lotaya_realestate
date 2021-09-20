from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def validate(arr,data):
    temp={}
    for i in arr:
        if data.get(i):
            temp[i]=data.get(i)
        else:
            return False
    return temp

def check_fake_admin(fn):
    # def warper(request,*args,**kargs):
    #     if request.user.is_authenticated:
            
    #         if request.user.groups.filter(name='fake_admin').exists():
    #             return fn()
    #         return redirect('authenticate:login')
    # return warper()
    decorator=user_passes_test(lambda u: u.groups.filter(name='fake_admin').exists() and u.is_authenticated)
    if fn:
        return decorator(fn)
    return decorator