# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack_plot', '0009_auto_20150703_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='SshHackLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=6)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='sshhacklocation',
            unique_together=set([('longitude', 'latitude')]),
        ),
        migrations.RemoveField(
            model_name='sshhackip',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='sshhackip',
            name='longitude',
        ),
        migrations.AddField(
            model_name='sshhackip',
            name='location',
            field=models.ForeignKey(default=1, to='hack_plot.SshHackLocation'),
            preserve_default=False,
        ),
    ]
