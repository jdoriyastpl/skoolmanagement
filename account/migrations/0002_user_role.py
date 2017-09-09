# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-09 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('principal', 'Principal'), ('teacher', 'Teacher'), ('staff', 'Staff')], default='principal', max_length=1, verbose_name='login as a '),
        ),
    ]
