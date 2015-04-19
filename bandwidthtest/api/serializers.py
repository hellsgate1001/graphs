from rest_framework import serializers

from ..models import BandwidthTest

class BandwidthTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandwidthTest
        fields = ('test_start', 'test_end', 'dlspeed', 'ulspeed', 'measure')
