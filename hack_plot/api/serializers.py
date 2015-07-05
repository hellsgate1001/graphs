from rest_framework import serializers

from ..models import SshHackIP, SshHackLocation


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
            'located',
            'attempts'
        ]


class HackLocationSerializer(serializers.ModelSerializer):
    ip_addresses = serializers.SerializerMethodField()

    def get_ip_addresses(self, obj):
        return [HackIpSerializer(ip).data for ip in obj.sshhackip_set.all()]

    class Meta:
        model = SshHackLocation
        fields = [
            'id',
            'longitude',
            'latitude',
            'city',
            'region_code',
            'region_name',
            'time_zone',
            'country_code',
            'country_name',
            'zip_code',
            'ip_addresses'
        ]
