# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20141012_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledmeal',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
