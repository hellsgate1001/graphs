# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack_plot', '0010_auto_20150705_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sshhackip',
            name='city',
        ),
        migrations.RemoveField(
            model_name='sshhackip',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='sshhackip',
            name='country_name',
        ),
        migrations.RemoveField(
            model_name='sshhackip',
            name='region_code',
        ),
        migrations.RemoveField(
            model_name='sshhackip',
            name='region_name',
        ),
        migrations.RemoveField(
            model_name='sshhackip',
            name='time_zone',
        ),
        migrations.RemoveField(
            model_name='sshhackip',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='sshhacklocation',
            name='city',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sshhacklocation',
            name='country_code',
            field=models.CharField(max_length=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sshhacklocation',
            name='country_name',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sshhacklocation',
            name='region_code',
            field=models.CharField(max_length=4, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sshhacklocation',
            name='region_name',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sshhacklocation',
            name='time_zone',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sshhacklocation',
            name='zip_code',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
    ]
