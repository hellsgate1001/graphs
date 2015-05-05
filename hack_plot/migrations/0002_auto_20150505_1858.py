# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack_plot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SshHackAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attempted', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SshHackIP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('city', models.CharField(max_length=255, blank=True)),
                ('region_code', models.CharField(max_length=2, blank=True)),
                ('region_name', models.CharField(max_length=255, blank=True)),
                ('time_zone', models.CharField(max_length=255, blank=True)),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=6)),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=6)),
                ('country_code', models.CharField(max_length=2, blank=True)),
                ('country_name', models.CharField(max_length=255, blank=True)),
                ('zip_code', models.CharField(max_length=15, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SshHackUsername',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='SshHack',
        ),
        migrations.AddField(
            model_name='sshhackattempt',
            name='ip',
            field=models.ForeignKey(to='hack_plot.SshHackIP'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sshhackattempt',
            name='username',
            field=models.ForeignKey(to='hack_plot.SshHackUsername'),
            preserve_default=True,
        ),
    ]
