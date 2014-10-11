# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_recipe_steps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='steps',
        ),
        migrations.AddField(
            model_name='recipe',
            name='steps_json',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
