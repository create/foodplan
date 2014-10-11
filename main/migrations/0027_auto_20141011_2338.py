# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_scheduledmeal_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='detailed_json',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='price',
            field=models.DecimalField(default=5.0, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scheduledmeal',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 10, 11, 23, 38, 58, 300135)),
        ),
    ]
