from django.db import models


class SshHackIP(models.Model):
    ip_address = models.GenericIPAddressField()
    city = models.CharField(max_length=255, blank=True)
    region_code = models.CharField(max_length=2, blank=True)
    region_name = models.CharField(max_length=255, blank=True)
    time_zone = models.CharField(max_length=255, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    country_code = models.CharField(max_length=2, blank=True)
    country_name = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)

    def __unicode__(self):
        return self.ip


class SshHackUsername(models.Model):
    username = models.CharField(max_length=255)

    def __unicode__(self):
        return self.username


class SshHackAttempt(models.Model):
    attempted = models.DateTimeField()
    ip = models.ForeignKey(SshHackIP)
    username = models.ForeignKey(SshHackUsername)

    def __unicode__(self):
        return '{atempted} - {ip}'.format(
            attempted=self.attempted.strftime('%Y-%m-%d %H:%M:%S'),
            ip=self.ip.ip_address
        )
