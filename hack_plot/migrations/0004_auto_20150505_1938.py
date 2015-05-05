# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack_plot', '0003_auto_20150505_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sshhackip',
            name='ip_address',
            field=models.GenericIPAddressField(unique=True),
            preserve_default=True,
        ),
    ]
