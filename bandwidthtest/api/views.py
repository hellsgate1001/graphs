from rest_framework import generics

from .serializers import BandwidthTestSerializer
from ..models import BandwidthTest


class BandwidthTestList(generics.ListCreateAPIView):
    queryset = BandwidthTest.objects.all()
    serializer_class = BandwidthTestSerializer


class BandwidthTestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BandwidthTest.objects.all()
    serializer_class = BandwidthTestSerializer
