# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-03-13 18:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0027_auto_20170221_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='world',
            old_name='canvas_ids',
            new_name='external_ids',
        ),
    ]
