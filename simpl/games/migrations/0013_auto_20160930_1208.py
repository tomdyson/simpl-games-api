# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-30 12:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0012_scenario_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ('order',), 'verbose_name': 'period', 'verbose_name_plural': 'periods'},
        ),
    ]
