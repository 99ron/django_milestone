# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-31 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_auto_20191031_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='car_model',
            field=models.CharField(max_length=30),
        ),
    ]