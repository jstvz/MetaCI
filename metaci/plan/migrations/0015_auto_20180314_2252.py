# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-14 22:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0014_auto_20180302_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='planrepository',
            options={'ordering': ['repo', 'plan'], 'verbose_name_plural': 'Plan Repositories'},
        ),
    ]
