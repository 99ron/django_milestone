# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-16 23:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20190915_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='lastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
    ]
