# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack_plot', '0008_sshhackattempt_ssh_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sshhackattempt',
            name='ssh_id',
            field=models.PositiveIntegerField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
