# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-19 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='no_students',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
