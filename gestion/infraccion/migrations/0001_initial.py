# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-17 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Infraccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, verbose_name=b'N\xc3\xbamero de Identificaci\xc3\xb3n')),
                ('sede', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True, verbose_name=b'Descripci\xc3\xb3n')),
                ('placa', models.CharField(max_length=6)),
                ('fecha', models.DateField()),
            ],
            options={
                'ordering': ['sede'],
                'verbose_name_plural': 'Infracciones',
            },
        ),
    ]
