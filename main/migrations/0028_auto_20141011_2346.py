# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20141011_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledmeal',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 10, 11, 23, 46, 59, 469694)),
        ),
    ]
