# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-18 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0022_auto_20161006_1503'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scenario',
            unique_together=set([]),
        ),
    ]
