from django.urls import path
from .views import about, detail, home,showroom,find

app_name='core'
urlpatterns=[
    path('',home,name='home'),
    path('about',about,name='about'),
    path('showroom', showroom,name='showroom'),
    path('find',find,name='find'),
    path('detail/<slug>' ,detail,name='detail')
]