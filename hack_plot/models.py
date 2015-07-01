import requests
import json

from django.db import models
from django.utils import timezone


class SshHackIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    city = models.CharField(max_length=255, blank=True)
    region_code = models.CharField(max_length=2, blank=True)
    region_name = models.CharField(max_length=255, blank=True)
    time_zone = models.CharField(max_length=255, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    country_code = models.CharField(max_length=2, blank=True)
    country_name = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)
    located = models.BooleanField(default=False)

    def __unicode__(self):
        return self.ip_address

    def get_geoip_data(self):
        response = requests.get(
            'http://127.0.0.1:8080/json/{ip}'.format(ip=self.ip_address)
        )
        response.raise_for_status()
        return json.loads(response.content)

    def set_location(self):
        if self.located:
            return

        location = self.get_geoip_data()
        for k, v in location.items():
            if k in self._meta.fields:
                setattr(self, k, v)
        self.located = True
        self.save()


class SshHackUsername(models.Model):
    username = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.username


class SshHackAttempt(models.Model):
    attempted = models.DateTimeField()
    ip = models.ForeignKey(SshHackIP)
    username = models.ForeignKey(SshHackUsername)

    def __unicode__(self):
        return '{attempted} - {ip}'.format(
            attempted=self.attempted.strftime('%Y-%m-%d %H:%M:%S'),
            ip=self.ip.ip_address
        )

    def save(self, *args, **kwargs):
        if not timezone.is_aware(self.attempted):
            timezone.make_aware(self.attempted, timezone.get_current_timezone())
        super(SshHackAttempt, self).save(*args, **kwargs)
