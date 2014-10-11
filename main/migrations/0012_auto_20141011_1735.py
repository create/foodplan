# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_recipe_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_vegetarian',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
