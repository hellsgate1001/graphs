# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack_plot', '0005_auto_20150505_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='sshhackip',
            name='located',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
