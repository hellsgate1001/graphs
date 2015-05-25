# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandwidthtest', '0002_auto_20150525_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandwidthtest',
            name='test_start',
            field=models.DateTimeField(unique=True),
            preserve_default=True,
        ),
    ]
