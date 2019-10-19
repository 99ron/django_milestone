# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-04 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191004_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='wrap_colour',
            field=models.CharField(default='black', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='services',
            name='damage',
            field=models.CharField(blank=True, max_length=240),
        ),
    ]