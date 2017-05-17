# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizaciones', '0003_auto_20170517_0858'),
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AumentadoIngresos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.IntegerField(choices=[(1, 'Caf\xe9'), (2, 'Cacao'), (3, 'Hostalizas')])),
                ('valor', models.FloatField()),
            ],
            options={
                'verbose_name_plural': '34.3 Cantidad de productores aumentado ingresos',
            },
        ),
        migrations.CreateModel(
            name='AumentadoProductividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
            ],
            options={
                'verbose_name_plural': '35 productividad (kg/ha) de cacao fermentado seco',
            },
        ),
        migrations.CreateModel(
            name='DesempenoFinanciero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opciones', models.IntegerField(choices=[(1, 'Balance General'), (2, 'Estado de resultado'), (3, 'P\xe9rdidas y ganancias')])),
                ('valor', models.FloatField()),
                ('mejoras', models.TextField(verbose_name='Principales Mejoras Realizadas (Describa)')),
                ('limitante', models.TextField(verbose_name='Principales \xc1reas a Mejorar/Limitantes (Describa)')),
            ],
            options={
                'verbose_name': '5. Desempe\xf1o financiero',
                'verbose_name_plural': '5. Desempe\xf1o financiero',
            },
        ),
        migrations.CreateModel(
            name='Digitador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Facilitadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opciones', models.IntegerField(choices=[(1, 'Desarrolladores de capacidades y ONG'), (2, 'Proveedores de servicios'), (3, 'Organizaciones del sector'), (4, 'Comunidad'), (5, 'Gobierno y regulaciones')])),
                ('valor', models.FloatField()),
                ('mejoras', models.TextField(verbose_name='Principales Mejoras Realizadas (Describa)')),
                ('limitante', models.TextField(verbose_name='Principales \xc1reas a Mejorar/Limitantes (Describa)')),
            ],
            options={
                'verbose_name': '9. Facilitadores',
                'verbose_name_plural': '9. Facilitadores',
            },
        ),
        migrations.CreateModel(
            name='GestionFinanciera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opciones', models.IntegerField(choices=[(1, 'Gesti\xf3n financiera'), (2, 'Planificaci\xf3n financiera'), (3, 'Registro de informaci\xf3n y monitoreo')])),
                ('valor', models.FloatField()),
                ('mejoras', models.TextField(verbose_name='Principales Mejoras Realizadas (Describa)')),
                ('limitante', models.TextField(verbose_name='Principales \xc1reas a Mejorar/Limitantes (Describa)')),
            ],
            options={
                'verbose_name': '4. Gesti\xf3n financiera',
                'verbose_name_plural': '4. Gesti\xf3n financiera',
            },
        ),
        migrations.CreateModel(
            name='GestionInterna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opciones', models.IntegerField(choices=[(1, 'Gobernabilidad'), (2, 'Organizaci\xf3n interna'), (3, 'Planificaci\xf3n de negocios')])),
                ('valor', models.FloatField()),
                ('mejoras', models.TextField(verbose_name='Principales Mejoras Realizadas (Describa)')),
                ('limitante', models.TextField(verbose_name='Principales \xc1reas a Mejorar/Limitantes (Describa)')),
            ],
            options={
                'verbose_name': '1.Gesti\xf3n Interna',
                'verbose_name_plural': '1.Gesti\xf3n Interna',
            },
        ),
        migrations.CreateModel(
            name='IncrementoAbastecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprador', models.FloatField()),
                ('tipo_mercado', multiselectfield.db.fields.MultiSelectField(choices=[('uno', 'Tradicional'), ('dos', 'Feria'), ('tres', 'Local'), ('cuatro', 'Empresa comercializadora'), ('cinco', 'Empresa procesadora'), ('seis', 'Empresas exportadoras'), ('siete', 'Supermercado'), ('ocho', 'Cadena de restaurantes'), ('nueve', 'Intermediarios')], max_length=47)),
            ],
            options={
                'verbose_name_plural': '34.2 Cantidad de productores que incremento de volumen',
            },
        ),
        migrations.CreateModel(
            name='Mercados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opciones', models.IntegerField(choices=[(1, 'Riesgo relacionado con el mercado'), (2, 'Log\xedstica de salida'), (3, 'Estrategias de mercadeo')])),
                ('valor', models.FloatField()),
                ('mejoras', models.TextField(verbose_name='Principales Mejoras Realizadas (Describa)')),
                ('limitante', models.TextField(verbose_name='Principales \xc1reas a Mejorar/Limitantes (Describa)')),
            ],
            options={
                'verbose_name': '7. Mercados',
                'verbose_name_plural': '7. Mercados',
            },
        ),
        migrations.CreateModel(
            name='Operaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opciones', models.IntegerField(choices=[(1, 'Logistica, almacenamiento y tecnolog\xeda'), (2, 'Producci\xf3n'), (3, 'Procesamiento')])),
                ('valor', models.FloatField()),
                ('mejoras', models.TextField(verbose_name='Principales Mejoras Realizadas (Describa)')),
                ('limitante', models.TextField(verbose_name='Principales \xc1reas a Mejorar/Limitantes (Describa)')),
            ],
            options={
                'verbose_name': '2. Operaciones',
                'verbose_name_plural': '2. Operaciones',
            },
        ),
        migrations.CreateModel(
            name='ProducenComercializan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.IntegerField(choices=[(1, 'a) Producen y comercializan de forma colectiva'), (2, 'b) Producen productos sanos'), (3, 'c) Tienen contratos de largo plazo'), (4, 'c.1) Contrato escrito'), (5, 'c.2) Contrato verbal'), (6, 'c.3.) Periodo del contrato')])),
                ('cantidad_hombres', models.IntegerField()),
                ('cantidad_mujeres', models.IntegerField()),
                ('cultivo', models.CharField(max_length=250)),
                ('area_hombre_sembrada', models.FloatField()),
                ('area_mujer_sembrada', models.FloatField()),
                ('area_hombre_cosechada', models.FloatField()),
                ('area_mujer_cosechada', models.FloatField()),
                ('unidad_medida', models.CharField(max_length=50)),
                ('cantidad', models.FloatField()),
                ('cantidad_certificada', models.FloatField()),
                ('precio_promedio', models.FloatField()),
            ],
            options={
                'verbose_name_plural': '34.1 Productores que producen y comercializan de forma colectiva',
            },
        ),
        migrations.CreateModel(
            name='ResultadosEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('year', models.IntegerField(editable=False)),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.Digitador')),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizaciones.Organizacion')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugar.Pais')),
            ],
            options={
                'verbose_name': 'V. Resultados de evaluaci\xf3n SCOPE Pro',
                'verbose_name_plural': 'V. Resultados de evaluaci\xf3n SCOPE Pro',
            },
        ),
        migrations.CreateModel(
            name='ResultadosImplementacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('para_quien', models.IntegerField(choices=[(1, 'Adultos mayores de 35 a\xf1os'), (2, 'J\xf3venes menores de 35 a\xf1os')])),
                ('year', models.IntegerField(editable=False)),
                ('digitador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.Digitador')),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizaciones.Organizacion')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugar.Pais')),
            ],
            options={
                'verbose_name': 'VI. Resultados implementaci\xf3n del programa',
                'verbose_name_plural': 'VI. Resultados implementaci\xf3n del programa',
            },
        ),
        migrations.CreateModel(
            name='RiesgoExternos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opciones', models.IntegerField(choices=[(1, 'Conocimiento de riesgos nat. y climat.'), (2, 'Mitigaci\xf3n de riesgos nat. y climat.'), (3, 'Conocimiento de riesgos biol. y amb.'), (4, 'Mitigaci\xf3n de riesgos biol\xf3gicos y amb.')])),
                ('valor', models.FloatField()),
                ('mejoras', models.TextField(verbose_name='Principales Mejoras Realizadas (Describa)')),
                ('limitante', models.TextField(verbose_name='Principales \xc1reas a Mejorar/Limitantes (Describa)')),
                ('resultado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosEvaluacion')),
            ],
            options={
                'verbose_name': '8.Riesgo externo',
                'verbose_name_plural': '8.Riesgo externo',
            },
        ),
        migrations.CreateModel(
            name='Sostenibilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opciones', models.IntegerField(choices=[(1, 'Aspectos Sociales'), (2, 'Aspectos ambientales')])),
                ('valor', models.FloatField()),
                ('mejoras', models.TextField(verbose_name='Principales Mejoras Realizadas (Describa)')),
                ('limitante', models.TextField(verbose_name='Principales \xc1reas a Mejorar/Limitantes (Describa)')),
                ('resultado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosEvaluacion')),
            ],
            options={
                'verbose_name': '3. Sostenibilidad',
                'verbose_name_plural': '3. Sostenibilidad',
            },
        ),
        migrations.CreateModel(
            name='Suministros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opciones', models.IntegerField(choices=[(1, 'Adquisici\xf3n'), (2, 'Log\xedstica de entrada'), (3, 'Contrataci\xf3n de miembros/agr. Ext.'), (4, 'Supervisi\xf3n y cap.de productores'), (5, 'Servicios financieros a miembros')])),
                ('valor', models.FloatField()),
                ('mejoras', models.TextField(verbose_name='Principales Mejoras Realizadas (Describa)')),
                ('limitante', models.TextField(verbose_name='Principales \xc1reas a Mejorar/Limitantes (Describa)')),
                ('resultado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosEvaluacion')),
            ],
            options={
                'verbose_name': '6. Suministro',
                'verbose_name_plural': '6. Suministro',
            },
        ),
        migrations.AddField(
            model_name='producencomercializan',
            name='resultado_implementacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosImplementacion'),
        ),
        migrations.AddField(
            model_name='operaciones',
            name='resultado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosEvaluacion'),
        ),
        migrations.AddField(
            model_name='mercados',
            name='resultado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosEvaluacion'),
        ),
        migrations.AddField(
            model_name='incrementoabastecimiento',
            name='resultado_implementacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosImplementacion'),
        ),
        migrations.AddField(
            model_name='gestioninterna',
            name='resultado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosEvaluacion'),
        ),
        migrations.AddField(
            model_name='gestionfinanciera',
            name='resultado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosEvaluacion'),
        ),
        migrations.AddField(
            model_name='facilitadores',
            name='resultado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosEvaluacion'),
        ),
        migrations.AddField(
            model_name='desempenofinanciero',
            name='resultado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosEvaluacion'),
        ),
        migrations.AddField(
            model_name='aumentadoproductividad',
            name='resultado_implementacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosImplementacion'),
        ),
        migrations.AddField(
            model_name='aumentadoingresos',
            name='resultado_implementacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.ResultadosImplementacion'),
        ),
    ]
