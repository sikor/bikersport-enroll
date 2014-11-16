# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollapp', '0005_auto_20141115_2158'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('user', 'term')]),
        ),
    ]
