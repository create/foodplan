# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_ingredient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='Alpha_Carot_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Beta_Carot_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Beta_Crypt_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Calcium_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Carbohydrt_g',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Cholestrl_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Choline_Tot_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Copper_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='FA_Mono_g',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='FA_Poly_g',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='FA_Sat_g',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Fiber_TD_g',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Folate_DFE_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Folate_Tot_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Folic_Acid_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Food_Folate_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='GmWt_1',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='GmWt_2',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Iron_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Lut_Zea_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Lycopene_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Magnesium_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Manganese_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Niacin_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Panto_Acid_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Phosphorus_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Potassium_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Refuse_Pct',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Retinol_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Riboflavin_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Selenium_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Sodium_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Sugar_Tot_g',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Thiamin_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Vit_A_IU',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Vit_A_RAE',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Vit_B12_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Vit_B6_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Vit_C_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Vit_D_IU',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Vit_D_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Vit_E_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Vit_K_mig',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='Zinc_mg',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ash_g',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='energy_Kcal',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='lipid_total_g',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='protein_g',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='water_g',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
    ]
