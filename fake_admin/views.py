from django.http import response
from django.shortcuts import render

# Create your views here.
def create_house(request):
    if request.method=='POST':
        return response('ok')
    return render(request,'fakeadmin/')

def freeze_user(request):
    return render(request,'')

def list_user(request):
    return render(request=request)

def delete_user(request):
    return render(request=request)

def notification_list(request):
    return render(request)