from django.db import models


class SshHack(models.Model):
    ip = models.GenericIPAddressField()
    attempted = models.DateTimeField()
    username = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    region_code = models.CharField(max_length=2, blank=True)
    region_name = models.CharField(max_length=255, blank=True)
    time_zone = models.CharField(max_length=255, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    country_code = models.CharField(max_length=2, blank=True)
    country_name = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)
    attempts = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return '{ip} ({attempts} attempts)'.format(
            ip=self.ip, attempts=self.get_attempts
        )

    def get_attempts(self):
        return self.attempts or 0
