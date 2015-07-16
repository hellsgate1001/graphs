from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

try:
    import simplejson as json
except ImportError as e:
    import json

from rest_framework.renderers import JSONRenderer
from unipath import Path

from ...api.serializers import HackLocationSerializer
from ...cron import parse_auth_log
from ...models import SshHackLocation

class Command(BaseCommand):
    def handle(self, *args, **options):
        parse_auth_log()
        # Write the attempt data to json for fast AJAX loading
        serializer = HackLocationSerializer(SshHackLocation.objects.all(), many=True)
        data = JSONRenderer().render(serializer.data, 'application/json', {})
        json_output_file = Path(settings.STATIC_ROOT).child('hack_location.json')
        with open(json_output_file, 'wb') as f:
            f.write(data)
