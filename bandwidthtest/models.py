from django.db import models


class BandwidthTest(models.Model):
    test_start = models.DateTimeField(auto_now_add=True)
    test_end = models.DateTimeField(blank=True, null=True)
    dlspeed = models.DecimalField(max_digits=30, decimal_places=20, blank=True, null=True)
    ulspeed = models.DecimalField(max_digits=30, decimal_places=20, blank=True, null=True)
    measure = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return 'Start - {test_start}'.format(
            test_start=self.test_start.strftime('%Y-%m-%d %H:%M:%S')
        )
