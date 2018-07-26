# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-25 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import staszic.languages.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contests', '0011_auto_20180630_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages_desc', staszic.languages.fields.LanguageSelectionField()),
                ('problem_instance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contests.Contest')),
            ],
            options={
                'verbose_name': 'language config',
                'verbose_name_plural': 'language configs',
            },
        ),
    ]
