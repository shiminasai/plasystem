# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-02 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsectores', '0005_auto_20170921_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicadores',
            name='codigo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='ejecucion_mayor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='ejecucion_menor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='programatico_mayor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='indicadores',
            name='programatico_menor',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
