# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack_plot', '0007_auto_20150701_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='sshhackattempt',
            name='ssh_id',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
