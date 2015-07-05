from django.core.management.base import BaseCommand, CommandError

from ...cron import parse_auth_log

class Command(BaseCommand):
    def handle(self, *args, **options):
        parse_auth_log()
