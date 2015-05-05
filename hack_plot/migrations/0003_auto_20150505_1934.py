# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack_plot', '0002_auto_20150505_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sshhackip',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sshhackip',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True),
            preserve_default=True,
        ),
    ]
