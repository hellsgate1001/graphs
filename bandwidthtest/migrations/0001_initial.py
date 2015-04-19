# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandwidthTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_start', models.DateTimeField(auto_now_add=True)),
                ('test_end', models.DateTimeField(null=True, blank=True)),
                ('dlspeed', models.DecimalField(null=True, max_digits=30, decimal_places=20, blank=True)),
                ('ulspeed', models.DecimalField(null=True, max_digits=30, decimal_places=20, blank=True)),
                ('measure', models.CharField(max_length=20, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
