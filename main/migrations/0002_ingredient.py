# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('water_g', models.FloatField()),
                ('energy_Kcal', models.FloatField()),
                ('protein_g', models.FloatField()),
                ('lipid_total_g', models.FloatField()),
                ('ash_g', models.FloatField()),
                ('Carbohydrt_g', models.FloatField()),
                ('Fiber_TD_g', models.FloatField()),
                ('Sugar_Tot_g', models.FloatField()),
                ('Calcium_mg', models.FloatField()),
                ('Iron_mg', models.FloatField()),
                ('Magnesium_mg', models.FloatField()),
                ('Phosphorus_mg', models.FloatField()),
                ('Potassium_mg', models.FloatField()),
                ('Sodium_mg', models.FloatField()),
                ('Zinc_mg', models.FloatField()),
                ('Copper_mg', models.FloatField()),
                ('Manganese_mg', models.FloatField()),
                ('Selenium_mig', models.FloatField()),
                ('Vit_C_mg', models.FloatField()),
                ('Thiamin_mg', models.FloatField()),
                ('Riboflavin_mg', models.FloatField()),
                ('Niacin_mg', models.FloatField()),
                ('Panto_Acid_mg', models.FloatField()),
                ('Vit_B6_mg', models.FloatField()),
                ('Folate_Tot_mig', models.FloatField()),
                ('Folic_Acid_mig', models.FloatField()),
                ('Food_Folate_mig', models.FloatField()),
                ('Folate_DFE_mig', models.FloatField()),
                ('Choline_Tot_mg', models.FloatField()),
                ('Vit_B12_mig', models.FloatField()),
                ('Vit_A_IU', models.FloatField()),
                ('Vit_A_RAE', models.FloatField()),
                ('Retinol_mig', models.FloatField()),
                ('Alpha_Carot_mig', models.FloatField()),
                ('Beta_Carot_mig', models.FloatField()),
                ('Beta_Crypt_mig', models.FloatField()),
                ('Lycopene_mig', models.FloatField()),
                ('Lut_Zea_mig', models.FloatField()),
                ('Vit_E_mg', models.FloatField()),
                ('Vit_D_mig', models.FloatField()),
                ('Vit_D_IU', models.FloatField()),
                ('Vit_K_mig', models.FloatField()),
                ('FA_Sat_g', models.FloatField()),
                ('FA_Mono_g', models.FloatField()),
                ('FA_Poly_g', models.FloatField()),
                ('Cholestrl_mg', models.FloatField()),
                ('GmWt_1', models.FloatField()),
                ('GmWt_Desc1', models.CharField(max_length=255)),
                ('GmWt_2', models.FloatField()),
                ('GmWt_Desc2', models.CharField(max_length=255)),
                ('Refuse_Pct', models.FloatField()),
                ('foodgroup', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
