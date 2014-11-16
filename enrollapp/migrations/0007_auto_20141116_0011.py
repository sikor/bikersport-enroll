# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollapp', '0006_auto_20141115_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='endtime',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='term',
            name='starttime',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
