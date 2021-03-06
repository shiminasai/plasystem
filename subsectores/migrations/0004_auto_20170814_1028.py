# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-14 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('subsectores', '0003_auto_20170814_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='informemensual',
            name='resultados',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='informemensual',
            name='indicador',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='resultado', chained_model_field='objetivo', on_delete=django.db.models.deletion.CASCADE, to='subsectores.Indicadores'),
        ),
        migrations.AlterField(
            model_name='informemensual',
            name='intervencion',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='proyecto', chained_model_field='proyecto', on_delete=django.db.models.deletion.CASCADE, to='subsectores.Intervenciones'),
        ),
        migrations.AlterField(
            model_name='informemensual',
            name='resultado',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='intervencion', chained_model_field='intervencion', on_delete=django.db.models.deletion.CASCADE, to='subsectores.ObjetivosResultados'),
        ),
    ]
