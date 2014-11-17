# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import enrollapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollapp', '0008_auto_20141116_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='height',
            field=models.IntegerField(verbose_name='Wzrost [cm]', validators=[enrollapp.models.validate_height]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='weight',
            field=models.IntegerField(verbose_name='Waga [kg]', validators=[enrollapp.models.validate_weight]),
            preserve_default=True,
        ),
    ]
