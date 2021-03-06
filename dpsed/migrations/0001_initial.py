# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 09:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sap_no', models.CharField(blank=True, max_length=36, null=True)),
                ('title', models.CharField(max_length=36)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('contect', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_ext', models.CharField(blank=True, max_length=100, null=True)),
                ('faxno', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('invalid', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CycleStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=36)),
                ('invalid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sap_no', models.CharField(max_length=36)),
                ('product_desc', models.CharField(max_length=36)),
                ('specification', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now=True)),
                ('cycle_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dpsed.CycleStatus')),
            ],
        ),
        migrations.CreateModel(
            name='SaleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_user', models.CharField(max_length=60)),
                ('ord_date', models.DateField()),
                ('customer_title', models.CharField(max_length=60)),
                ('ships_order', models.CharField(max_length=16)),
                ('ord_amount', models.IntegerField(default=1)),
                ('delivery', models.DateField()),
                ('memo', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dpsed.Product')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zmms', models.CharField(blank=True, max_length=30, null=True)),
                ('recevice_date', models.DateField(auto_now=True)),
                ('material_ctrl', models.CharField(blank=True, max_length=30, null=True)),
                ('workday', models.IntegerField(default=1)),
                ('ships_order', models.CharField(max_length=16)),
                ('work_order', models.CharField(max_length=16)),
                ('ord_amount', models.IntegerField(default=1)),
                ('deliverly', models.DateField(blank=True, null=True)),
                ('material_ready_date', models.DateField(blank=True, null=True)),
                ('estimated_finish', models.DateField(blank=True, null=True)),
                ('reuqest_user', models.CharField(max_length=16)),
                ('material_duty', models.CharField(max_length=16)),
                ('comfirm', models.CharField(blank=True, max_length=30, null=True)),
                ('manage_memo', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dpsed.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dpsed.Product')),
            ],
        ),
    ]
