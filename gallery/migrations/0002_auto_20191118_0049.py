# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-18 00:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='user_int',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile'),
        ),
    ]