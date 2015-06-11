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

    class Meta:
        ordering = ['order',]


class Contact(models.Model):
    sender = models.CharField("Name", max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{sender}: {sent}'.format(
            sender=self.sender,
            sent=self.sent.strftime('%Y-%m-%d %H:%M:%S')
        )
