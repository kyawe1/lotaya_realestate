from django.urls import path,re_path
from .views import about, detail, home,showroom,find

app_name='core'
urlpatterns=[
    path('',home,name='home'),
    path('about',about,name='about'),
    path('showroom', showroom,name='showroom'),
    re_path(r'^find/',find,name='find'),
    path('detail/<slug>' ,detail,name='detail')
]