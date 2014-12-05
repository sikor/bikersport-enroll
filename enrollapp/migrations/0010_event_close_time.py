# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollapp', '0009_auto_20141117_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='close_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
