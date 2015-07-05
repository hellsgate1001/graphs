import requests
import json

from django.db import models
from django.utils import timezone


class SshHackLocation(models.Model):
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    city = models.CharField(max_length=255, blank=True)
    region_code = models.CharField(max_length=4, blank=True)
    region_name = models.CharField(max_length=255, blank=True)
    time_zone = models.CharField(max_length=255, blank=True)
    country_code = models.CharField(max_length=2, blank=True)
    country_name = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)

    def __unicode__(self):
        return '%s:%s' % (self.longitude, self.latitude)

    class Meta:
        unique_together = (('longitude', 'latitude'),)


class SshHackIP(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    location = models.ForeignKey(SshHackLocation)
    located = models.BooleanField(default=False)

    def __unicode__(self):
        return self.ip_address

    def get_geoip_data(self):
        response = requests.get(
            'http://127.0.0.1:8080/json/{ip}'.format(ip=self.ip_address)
        )
        response.raise_for_status()
        return json.loads(response.content)

    def save(self, *args, **kwargs):
        if not self.located:
            self.set_location(False)
        super(SshHackIP, self).save(*args, **kwargs)

    def set_location(self, save=True):
        if self.located:
            return

        location = self.get_geoip_data()
        ssh_location, created = SshHackLocation.objects.get_or_create(
            longitude=location['longitude'],
            latitude=location['latitude']
        )
        for k, v in location.items():
            if hasattr(ssh_location, k):
                if getattr(ssh_location, k) == '':
                    setattr(ssh_location, k, v)
        ssh_location.save()

        self.location = ssh_location
        self.located = True
        if save:
            self.save()


class SshHackUsername(models.Model):
    username = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.username


class SshHackAttempt(models.Model):
    attempted = models.DateTimeField()
    ip = models.ForeignKey(SshHackIP)
    username = models.ForeignKey(SshHackUsername)
    ssh_id = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def __unicode__(self):
        return '{attempted} - {ip}'.format(
            attempted=self.attempted.strftime('%Y-%m-%d %H:%M:%S'),
            ip=self.ip.ip_address
        )

    def save(self, *args, **kwargs):
        if not timezone.is_aware(self.attempted):
            self.attempted = timezone.make_aware(
                self.attempted, timezone.get_current_timezone()
            )
        super(SshHackAttempt, self).save(*args, **kwargs)
