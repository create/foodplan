# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_recipe_instructions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='instructions',
            new_name='steps',
        ),
    ]
