# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describe', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=100)),
                ('describe', models.TextField()),
                ('intranet_ip', models.CharField(max_length=100)),
                ('internet_ip', models.CharField(blank=True, max_length=100)),
                ('domain', models.BooleanField()),
                ('os', models.CharField(blank=True, max_length=100)),
                ('local_account', models.CharField(max_length=100)),
                ('local_password', models.CharField(max_length=100)),
                ('manage_account', models.CharField(blank=True, max_length=100)),
                ('manage_password', models.CharField(blank=True, max_length=100)),
                ('postion', models.CharField(max_length=100)),
                ('pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myserver.Pattern')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describe', models.CharField(max_length=100)),
                ('manage_method', models.CharField(max_length=100)),
                ('manage_account', models.CharField(max_length=100)),
                ('manage_password', models.CharField(max_length=100)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myserver.Server')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describe', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myserver.Status'),
        ),
    ]
