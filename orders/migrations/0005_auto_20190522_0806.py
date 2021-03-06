# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-22 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20190519_1653'),
        ('orders', '0004_auto_20190519_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.BillingProfile'),
        ),
    ]
