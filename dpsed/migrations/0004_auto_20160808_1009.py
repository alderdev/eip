# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsed', '0003_auto_20160805_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='recevice_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
