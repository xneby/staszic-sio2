# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-25 21:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reportconfig',
            options={'verbose_name': 'report element visible for the participant', 'verbose_name_plural': 'report elements visible for the participant'},
        ),
        migrations.RenameField(
            model_name='reportconfig',
            old_name='report_desc',
            new_name='element',
        ),
    ]
