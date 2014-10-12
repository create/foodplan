# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20141012_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useringredient',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='UserIngredient',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
