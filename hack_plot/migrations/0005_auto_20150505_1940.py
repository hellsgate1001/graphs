# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack_plot', '0004_auto_20150505_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sshhackusername',
            name='username',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
