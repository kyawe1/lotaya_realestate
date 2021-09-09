from django.urls import path,re_path
from .views import interest,create,delete

app_name='interest'
urlpatterns=[
    path('',interest,name='list'),
    re_path(r'^create/',create,name='create'),
    re_path(r'^delete/',delete,name='delete'),
]