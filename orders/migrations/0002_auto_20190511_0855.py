# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-11 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=100),
        ),
    ]
