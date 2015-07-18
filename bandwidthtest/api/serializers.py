from rest_framework import serializers

from ..models import BandwidthTest

class BandwidthTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandwidthTest
        fields = ('test_start', 'test_end', 'dlspeed', 'ulspeed', 'measure')


class BandwidthGroupedByDaySerializer(serializers.ModelSerializer):
    # sunday = serializers.SerializerMethodField()
    # monday = serializers.SerializerMethodField()
    # tuesday = serializers.SerializerMethodField()
    # wednesday = serializers.SerializerMethodField()
    # thursday = serializers.SerializerMethodField()
    # friday = serializers.SerializerMethodField()
    # saturday = serializers.SerializerMethodField()

    # all_days = None

    # def get_sunday(self, obj):
    #     if all_days is None:
    #         self.set_all_days(obj)

    # def set_all_days(self, obj):

    class Meta:
        model = BandwidthTest
        fields = (
            'sunday',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday'
        )
