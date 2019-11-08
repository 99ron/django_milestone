# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-08 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('paid', models.BooleanField(default=False)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Services')),
            ],
        ),
    ]
