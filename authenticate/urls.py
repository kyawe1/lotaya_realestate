from django.urls import path,include,re_path
from .views import login,logout,register


app_name='authentication'
urlpatterns=[
    re_path(r'^login',login,name='login'),
    re_path(r'^register',register,name='register'),
    path('logout',logout,name='logout'),
]