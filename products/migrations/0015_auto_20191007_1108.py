# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-07 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20191007_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]