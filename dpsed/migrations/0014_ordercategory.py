# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsed', '0013_delete_ordercategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=36)),
                ('order_squence', models.IntegerField(default=1000)),
                ('invalid', models.BooleanField(default=False)),
            ],
        ),
    ]
