# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('priority',)},
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
