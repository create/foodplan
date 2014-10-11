# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20141011_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=djorm_pgarray.fields.ArrayField(default=None, null=True, verbose_name=models.TextField(), blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_vegetarian',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time_seconds',
            field=models.IntegerField(default=1200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_json',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=1),
        ),
    ]
