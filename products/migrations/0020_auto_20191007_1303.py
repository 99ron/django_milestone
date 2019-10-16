# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-07 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20191007_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='damage',
        ),
        migrations.AddField(
            model_name='services',
            name='damage',
            field=models.ManyToManyField(to='products.Damage'),
        ),
        migrations.RemoveField(
            model_name='services',
            name='optional_service',
        ),
        migrations.AddField(
            model_name='services',
            name='optional_service',
            field=models.ManyToManyField(to='products.OptionalService'),
        ),
    ]
