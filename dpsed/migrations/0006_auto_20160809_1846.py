# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsed', '0005_auto_20160808_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='work_order',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
