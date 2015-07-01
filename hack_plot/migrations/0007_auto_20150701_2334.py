# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack_plot', '0006_sshhackip_located'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sshhackip',
            name='region_code',
            field=models.CharField(max_length=4, blank=True),
            preserve_default=True,
        ),
    ]
