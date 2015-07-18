from django.db.models import Count, Sum, Max, Min, Avg

from rest_framework import generics

from .serializers import BandwidthTestSerializer, BandwidthGroupedByDaySerializer
from ..models import BandwidthTest


class BandwidthTestList(generics.ListCreateAPIView):
    queryset = BandwidthTest.objects.all()
    serializer_class = BandwidthTestSerializer


class BandwidthTestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BandwidthTest.objects.all()
    serializer_class = BandwidthTestSerializer


class BandwidthGroupedByDay(generics.ListAPIView):
    serializer_class = BandwidthGroupedByDaySerializer

    def get_queryset(self):
        return (BandwidthTest.objects.all()
            .extra({'day': 'DAYNAME(test_start)'})
            .values('day')
            .annotate(
                Count('dlspeed'),
                Sum('dlspeed'),
                Max('dlspeed'),
                Min('dlspeed'),
                Avg('dlspeed')
            )
        )
