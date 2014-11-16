# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('enrollapp', '0002_auto_20141115_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='participant',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, default=None, related_name='terms'),
            preserve_default=True,
        ),
    ]
