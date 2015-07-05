from rest_framework import serializers

from ..models import SshHackIP


class HackIpSerializer(serializers.ModelSerializer):
    attempts = serializers.SerializerMethodField()

    def get_attempts(self, obj):
        return [
            {
                'id': x.id,
                'attempted': x.attempted,
                'ssh_id': x.ssh_id,
                'username': x.username.username
            } for x in obj.sshhackattempt_set.all().prefetch_related('username')
        ]

    class Meta:
        model = SshHackIP
        fields = [
            'id',
            'ip_address',
            'city',
            'region_code',
            'region_name',
            'time_zone',
            'longitude',
            'latitude',
            'country_code',
            'country_name',
            'zip_code',
            'located',
            'attempts'
        ]
