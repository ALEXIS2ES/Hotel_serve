# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-12 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_habitacion',
            name='nombre',
        ),
        migrations.AddField(
            model_name='tipo_habitacion',
            name='TipoHab',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]