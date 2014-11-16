# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('enrollapp', '0003_auto_20141115_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='participant',
            field=models.ForeignKey(blank=True, related_name='terms', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
