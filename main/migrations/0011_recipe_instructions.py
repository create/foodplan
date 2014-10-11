# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_recipe_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=djorm_pgarray.fields.ArrayField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
