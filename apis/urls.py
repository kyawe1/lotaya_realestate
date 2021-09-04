from django.urls import path ,include
from .router import router
app_name='apis'
urlpatterns=[
    path('',include(router.urls),name='router')
]