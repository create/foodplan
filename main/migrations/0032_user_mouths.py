# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20141012_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mouths',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
