# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models, migrations
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('urlname', models.CharField(unique=True, max_length=30)),
                ('is_open', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('event', models.ForeignKey(to='enrollapp.Event', related_name='terms')),
                ('participant', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='terms')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='details')),
            ],
            options={
            },
            bases=(models.Model,),
        )
    ]
