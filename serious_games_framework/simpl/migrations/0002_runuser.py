# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 18:58
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simpl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(blank=True)),
                ('facilitator', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='run_users', to='simpl.Role')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='run_users', to='simpl.Run')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='run_users', to=settings.AUTH_USER_MODEL)),
                ('world', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='run_users', to='simpl.World')),
            ],
            options={
                'verbose_name': 'run',
                'verbose_name_plural': 'runs',
            },
        ),
    ]