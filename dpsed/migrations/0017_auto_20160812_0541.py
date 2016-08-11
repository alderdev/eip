# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsed', '0016_auto_20160809_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='material_ctrl',
            field=models.ForeignKey(to='dpsed.MaterialCtrlOption', null=True, blank=True),
        ),
    ]
