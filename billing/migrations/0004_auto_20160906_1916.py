# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20160906_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture',
            field=models.PositiveIntegerField(),
        ),
    ]
