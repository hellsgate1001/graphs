# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphs', '0002_chart_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chart',
            options={'ordering': ['order']},
        ),
    ]
