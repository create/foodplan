# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20141011_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledMeal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipe_id', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime(2014, 10, 11, 23, 12, 22, 16354))),
                ('user_id', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('gender', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
