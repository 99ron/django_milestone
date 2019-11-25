# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-25 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_paymentdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.OrderList'),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='profiles.UserProfile'),
        ),
    ]
