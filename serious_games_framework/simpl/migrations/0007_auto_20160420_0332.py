# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpl', '0006_remove_period_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
