# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-04 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191003_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='type_of_service',
            field=models.CharField(max_length=100),
        ),
    ]
