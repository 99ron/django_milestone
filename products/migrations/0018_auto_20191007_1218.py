# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-07 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20191007_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='damage',
            field=models.ManyToManyField(to='products.Damage'),
        ),
    ]
