# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-18 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20191118_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='order_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='review_table', to='orders.OrderList'),
        ),
    ]