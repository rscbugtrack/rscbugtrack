# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-18 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackingapp', '0004_auto_20171118_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugtrack',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
