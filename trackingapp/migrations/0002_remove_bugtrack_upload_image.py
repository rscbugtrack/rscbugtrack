# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 17:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bugtrack',
            name='upload_image',
        ),
    ]
