# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_recipe_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=djorm_pgarray.fields.ArrayField(default=None, null=True, verbose_name=models.TextField(), blank=True),
            preserve_default=True,
        ),
    ]
