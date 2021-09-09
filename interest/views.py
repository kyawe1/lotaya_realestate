
from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http.request import HttpRequest
from django.core.paginator import Paginator
from .models import Interest
from core.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def interest(request:HttpRequest):
    i=Interest.objects.all()
    obj=Paginator(i,5)
    page_number=request.GET.get('page_number')
    h=obj.get_page(page_number)
    return render(request,"interest/list.html",{'list':h,'title':'Interest'})

@login_required
def create(request:HttpRequest):
    r=request.GET.get('p_id')
    print(r)
    if r:
        i=Product.objects.get(id=r)
        if i :
            obj=Interest.objects.create(owner=request.user,product=i)
            obj.save()
            return JsonResponse('ok',safe=False)
    return JsonResponse({'ok':'this is a book'},safe=False)
    
@login_required
def delete(request:HttpRequest):
    if request.GET.get('interest_id'):
        r=request.GET.get('interest_id')
        if r:
            i=Interest.objects.get(id=r)
            if i and i.owner==request.user:
                i.delete()
                
                return JsonResponse('ok',encoder=DjangoJSONEncoder,safe=False)
    elif request.GET.get('p_id'):
        r=request.GET.get('p_id')
        obj=request.user.interested.filter(product_id=r)
        if obj:
            obj.delete()
        return JsonResponse('ok',encoder=DjangoJSONEncoder,safe=False)
    return JsonResponse('not ok',encoder=DjangoJSONEncoder,safe=False)
    