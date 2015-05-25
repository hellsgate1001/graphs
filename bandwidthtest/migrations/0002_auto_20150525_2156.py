# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandwidthtest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandwidthtest',
            name='test_start',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
