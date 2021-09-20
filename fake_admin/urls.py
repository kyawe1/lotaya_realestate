from django.urls import path,re_path
from .views import create_house, list_user,notification_list,delete_user,freeze_user,list_house

app_name='fake_admin'
urlpatterns=[
    path('create',create_house,name='create_house'),
    path('list/user',list_user,name='list_user'),
    path('list/house',list_house,name='list_user'),
    path('list/user/<int:s>/freeze',freeze_user,name='freeze_user'),
    path('list/user/<int:s>/delete',delete_user,name='delete_user'),
    path('list/notified',notification_list,name='list_notified'),
]