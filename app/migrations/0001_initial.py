# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CIUDADES',
            fields=[
                ('cdepa', models.AutoField(serialize=False, primary_key=True)),
                ('cciuda', models.IntegerField()),
                ('nciudad', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CLIENTES',
            fields=[
                ('cclientes', models.AutoField(serialize=False, primary_key=True)),
                ('nombres', models.CharField(max_length=45)),
                ('cedula', models.IntegerField()),
                ('cciudad', models.ForeignKey(to='app.CIUDADES')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DEPARTAMENTOS',
            fields=[
                ('cdepa', models.AutoField(serialize=False, primary_key=True)),
                ('ndepa', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TIPODEDOCU',
            fields=[
                ('ctideid', models.AutoField(serialize=False, primary_key=True)),
                ('ntideid', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TIPOVEHICULOS',
            fields=[
                ('ctivehi', models.AutoField(serialize=False, primary_key=True)),
                ('ntivehi', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VEHICULOS',
            fields=[
                ('placas', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('color', models.CharField(max_length=45)),
                ('modelo', models.CharField(max_length=45)),
                ('capacidadpersonas', models.IntegerField()),
                ('cilindraje', models.CharField(max_length=45)),
                ('cclientes', models.ForeignKey(to='app.CLIENTES')),
                ('ctivehi', models.ForeignKey(to='app.TIPOVEHICULOS')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='clientes',
            name='cdepa',
            field=models.ForeignKey(to='app.DEPARTAMENTOS'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clientes',
            name='ctideid',
            field=models.ForeignKey(to='app.TIPODEDOCU'),
            preserve_default=True,
        ),
    ]
