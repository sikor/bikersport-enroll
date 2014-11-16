# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollapp', '0007_auto_20141116_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Wiek', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='height',
            field=models.IntegerField(verbose_name='Wzrost [cm]'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], null=True, max_length=6, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='weight',
            field=models.IntegerField(verbose_name='Waga [kg]'),
            preserve_default=True,
        ),
    ]
