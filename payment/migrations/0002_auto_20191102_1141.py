# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-02 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='country',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='full_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='postcode',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='street_address1',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='street_address2',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='town_city',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
