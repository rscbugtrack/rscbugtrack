# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 13:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trackingapp', '0005_auto_20171118_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_skills', models.CharField(help_text=b'Text your keyskil like python, Java or .net Developer', max_length=100)),
                ('experience', models.PositiveIntegerField(default=0)),
                ('programing_languages', models.CharField(help_text=b'List of progrming languages you know..', max_length=100)),
                ('databases', models.CharField(choices=[(b'M', b'MySql'), (b'S', b'Sql'), (b'O', b'Oracle'), (b'Sq', b'Sqlite3'), (b'P', b'PostgreSQL')], max_length=2)),
                ('designing', models.CharField(help_text=b'HTML, CSS, Bootstrap...etc', max_length=100)),
                ('scripting', models.CharField(help_text=b'Javascript, Jquery, AngularJS..etc', max_length=100)),
                ('tools', models.CharField(help_text=b'Like Pycharm, MySQL workbench...etc', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
