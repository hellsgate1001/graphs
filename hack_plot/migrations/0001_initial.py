# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SshHack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
                ('attempted', models.DateTimeField()),
                ('username', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=255, blank=True)),
                ('region_code', models.CharField(max_length=2, blank=True)),
                ('region_name', models.CharField(max_length=255, blank=True)),
                ('time_zone', models.CharField(max_length=255, blank=True)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=6)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=6)),
                ('country_code', models.CharField(max_length=2, blank=True)),
                ('country_name', models.CharField(max_length=255, blank=True)),
                ('zip_code', models.CharField(max_length=15, blank=True)),
                ('attempts', models.PositiveIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
