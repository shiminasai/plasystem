# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-24 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0005_auto_20170620_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizacion',
            name='tipo_rubro',
            field=models.IntegerField(blank=True, choices=[(1, 'Caf\xe9'), (2, 'Cacao'), (3, 'Hortaliza')], null=True, verbose_name='Tipo de rubro que es apoyado'),
        ),
        migrations.AlterField(
            model_name='empleadosorganizacion',
            name='adultos_hombre',
            field=models.IntegerField(verbose_name='Hombres adultos'),
        ),
        migrations.AlterField(
            model_name='empleadosorganizacion',
            name='adultos_mujer',
            field=models.IntegerField(verbose_name='Mujeres adultos'),
        ),
        migrations.AlterField(
            model_name='empleadosorganizacion',
            name='jovenes_hombre',
            field=models.IntegerField(verbose_name='Hombres j\xf3venes'),
        ),
        migrations.AlterField(
            model_name='empleadosorganizacion',
            name='jovenes_mujer',
            field=models.IntegerField(verbose_name='Mujeres j\xf3venes'),
        ),
        migrations.AlterField(
            model_name='empleadosorganizacion',
            name='total_hombre',
            field=models.IntegerField(verbose_name='Total de hombres'),
        ),
        migrations.AlterField(
            model_name='empleadosorganizacion',
            name='total_mujer',
            field=models.IntegerField(verbose_name='Total de mujeres'),
        ),
        migrations.AlterField(
            model_name='miembrosoficiales',
            name='activos_hombre',
            field=models.IntegerField(verbose_name='Hombres activos'),
        ),
        migrations.AlterField(
            model_name='miembrosoficiales',
            name='activos_mujer',
            field=models.IntegerField(verbose_name='Mujeres activas'),
        ),
        migrations.AlterField(
            model_name='miembrosoficiales',
            name='inactivos_hombre',
            field=models.IntegerField(verbose_name='Hombres inactivos'),
        ),
        migrations.AlterField(
            model_name='miembrosoficiales',
            name='inactivos_mujer',
            field=models.IntegerField(verbose_name='Mujeres inactivos'),
        ),
        migrations.AlterField(
            model_name='miembrosoficiales',
            name='jovenes_hombre',
            field=models.IntegerField(verbose_name='Hombres j\xf3venes'),
        ),
        migrations.AlterField(
            model_name='miembrosoficiales',
            name='jovenes_mujer',
            field=models.IntegerField(verbose_name='Mujeres j\xf3venes'),
        ),
        migrations.AlterField(
            model_name='miembrosoficiales',
            name='total_hombre',
            field=models.IntegerField(verbose_name='Total de hombres'),
        ),
        migrations.AlterField(
            model_name='miembrosoficiales',
            name='total_mujer',
            field=models.IntegerField(verbose_name='Total de mujeres'),
        ),
        migrations.AlterField(
            model_name='productoresproveedores',
            name='activos_hombre',
            field=models.IntegerField(verbose_name='Hombres activos'),
        ),
        migrations.AlterField(
            model_name='productoresproveedores',
            name='activos_mujer',
            field=models.IntegerField(verbose_name='Mujeres activos'),
        ),
        migrations.AlterField(
            model_name='productoresproveedores',
            name='jovenes_hombre',
            field=models.IntegerField(verbose_name='Hombres j\xf3venes'),
        ),
        migrations.AlterField(
            model_name='productoresproveedores',
            name='jovenes_mujer',
            field=models.IntegerField(verbose_name='Mujeres j\xf3venes'),
        ),
        migrations.AlterField(
            model_name='productoresproveedores',
            name='total_hombre',
            field=models.IntegerField(verbose_name='Total de hombres'),
        ),
        migrations.AlterField(
            model_name='productoresproveedores',
            name='total_mujer',
            field=models.IntegerField(verbose_name='Total de mujeres'),
        ),
    ]
