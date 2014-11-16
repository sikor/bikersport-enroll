# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enrollapp', '0004_auto_20141115_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('term', models.ForeignKey(related_name='enrollments', to='enrollapp.Term')),
                ('user', models.ForeignKey(related_name='enrollments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='term',
            name='participant',
        ),
        migrations.AddField(
            model_name='term',
            name='participants',
            field=models.ManyToManyField(through='enrollapp.Enrollment', related_name='terms', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='age',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='details'),
            preserve_default=True,
        ),
    ]
