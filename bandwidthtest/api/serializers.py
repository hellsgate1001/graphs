from rest_framework import serializers

from ..models import BandwidthTest

class BandwidthTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandwidthTest
        fields = ('test_start', 'test_end', 'dlspeed', 'ulspeed', 'measure')


class BandwidthGroupedByDaySerializer(serializers.Serializer):
    day = serializers.CharField(max_length=20)
    dlspeed__avg = serializers.DecimalField(max_digits=30, decimal_places=20)
    dlspeed__count = serializers.DecimalField(max_digits=30, decimal_places=20)
    dlspeed__max = serializers.DecimalField(max_digits=30, decimal_places=20)
    dlspeed__min = serializers.DecimalField(max_digits=30, decimal_places=20)
    dlspeed__sum = serializers.DecimalField(max_digits=30, decimal_places=20)
    ulspeed__avg = serializers.DecimalField(max_digits=30, decimal_places=20)
    ulspeed__count = serializers.DecimalField(max_digits=30, decimal_places=20)
    ulspeed__max = serializers.DecimalField(max_digits=30, decimal_places=20)
    ulspeed__min = serializers.DecimalField(max_digits=30, decimal_places=20)
    ulspeed__sum = serializers.DecimalField(max_digits=30, decimal_places=20)

    class Meta:
        model = BandwidthTest
        fields = (
            'day',
            'dlspeed__avg',
            'dlspeed__count',
            'dlspeed__max',
            'dlspeed__min',
            'dlspeed__sum',
            'ulspeed__avg',
            'ulspeed__count',
            'ulspeed__max',
            'ulspeed__min',
            'ulspeed__sum',
        )
