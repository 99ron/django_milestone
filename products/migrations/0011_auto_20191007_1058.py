# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-07 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20191007_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='damage',
            field=models.CharField(max_length=240),
        ),
    ]
