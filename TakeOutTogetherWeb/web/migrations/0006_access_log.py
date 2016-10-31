# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_update_file_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_time', models.DateTimeField(auto_now=True)),
                ('ip_address', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('user_agent', models.CharField(max_length=100)),
            ],
        ),
    ]