# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20141012_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient_id', models.IntegerField(default=1001)),
                ('user_id', models.ForeignKey(to='main.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
