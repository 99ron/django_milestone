# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-07 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20191007_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='id',
            field=models.AutoField(auto_created=True, default='1', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='services',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
