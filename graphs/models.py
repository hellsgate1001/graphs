from django.db import models

from django.utils.text import slugify


class Chart(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    order = models.PositiveSmallIntegerField(default=10)
    url = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.title

    @property
    def slugged_title(self):
        return slugify(self.title)
