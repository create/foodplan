# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_recipe_instructions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='instructions',
        ),
    ]
