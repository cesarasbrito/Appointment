# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppointmentApp', '0002_auto_20170407_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='hour',
            field=models.TimeField(),
        ),
    ]
