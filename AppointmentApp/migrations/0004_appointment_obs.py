# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppointmentApp', '0003_auto_20170407_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='obs',
            field=models.TextField(default='', max_length=300),
        ),
    ]
