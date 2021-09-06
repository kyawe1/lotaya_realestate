from django.urls import path
from .views import interest,create,delete

app_name='interest'
urlpatterns=[
    path('',interest,name='list'),
    path('create',create,name='create'),
    path('delete',delete,name='delete'),
]