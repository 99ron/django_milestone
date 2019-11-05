# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-31 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20191014_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='car_make',
            field=models.CharField(choices=[('audi', 'Audi'), ('bmw', 'BMW'), ('toyota', 'Toyota'), ('nissan', 'Nissan'), ('mini', 'Mini')], default='Audi', max_length=6),
        ),
    ]
