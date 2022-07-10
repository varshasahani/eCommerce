# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-19 16:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20190518_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingprofile',
            old_name='updated',
            new_name='update',
        ),
        migrations.AlterField(
            model_name='billingprofile',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='billingprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
