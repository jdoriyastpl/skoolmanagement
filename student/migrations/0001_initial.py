# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-12 11:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('standard', '0001_initial'),
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('father_name', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('religion', models.CharField(blank=True, choices=[('hindu', 'Hinduism'), ('muslim', 'Muslim'), ('christian', 'Christian'), ('sikh', 'Sikh')], max_length=10, verbose_name='Religion')),
                ('parents_primary_phone_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Length has to be 10', regex='^\\d{10}$')])),
                ('secondary_phone_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Length has to be 10', regex='^\\d{10}$')])),
                ('address', models.CharField(max_length=255)),
                ('picture', models.ImageField(blank=True, default='student/img/default.png', height_field='height_field', null=True, upload_to='', verbose_name='profile picture', width_field='width_field')),
                ('height_field', models.IntegerField(default=600, null=True)),
                ('width_field', models.IntegerField(default=600, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_section', to='section.Section')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_standard', to='standard.Standard')),
            ],
        ),
    ]
