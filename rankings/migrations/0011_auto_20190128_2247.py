# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-01-28 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0010_cachedrankingdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cachedrankingdata',
            name='data',
            field=models.BinaryField(),
        ),
    ]
