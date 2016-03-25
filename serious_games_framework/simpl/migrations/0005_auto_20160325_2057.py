# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 20:57
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpl', '0004_auto_20160325_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='world',
            name='current_phase',
        ),
        migrations.AddField(
            model_name='world',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]