# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20160906_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture',
            field=models.IntegerField(),
        ),
    ]
