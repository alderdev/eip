# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dpsed', '0009_auto_20160809_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workorder',
            name='order_category',
        ),
    ]