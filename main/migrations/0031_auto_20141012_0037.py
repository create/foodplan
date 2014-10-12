# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20141012_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledmeal',
            name='recipe_id',
            field=models.IntegerField(default=0),
        ),
    ]
