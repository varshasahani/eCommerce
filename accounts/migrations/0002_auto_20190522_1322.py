# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-22 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestemail',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
