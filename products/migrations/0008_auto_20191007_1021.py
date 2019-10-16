# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-07 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20191007_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='damage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Damage'),
        ),
        migrations.AlterField(
            model_name='services',
            name='optional_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.OptionalService'),
        ),
    ]
