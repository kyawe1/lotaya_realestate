from apis.models import Sample
from rest_framework.viewsets import ModelViewSet
from .serializers import SampleSerializer


class SampleViewSet(ModelViewSet):
    serializer_class=SampleSerializer
    queryset=Sample.objects.all()