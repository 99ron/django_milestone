# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-13 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20191113_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='review_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='gallery.Reviews'),
        ),
    ]
