from rest_framework.routers import DefaultRouter
from .viewset import SampleViewSet
router=DefaultRouter(trailing_slash='/?')

router.register(r'news',SampleViewSet)