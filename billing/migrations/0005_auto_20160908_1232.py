# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 12:32
from __future__ import unicode_literals

from django.db import migrations
from datetime import date, timedelta as td
import random


def fake_data_since_january(apps, schema_editor):
    Pricing = apps.get_model("billing", "Pricing")
    Lecture = apps.get_model("billing", "Lecture")
    january = date(2016, 1, 1)
    today = date.today()
    delta = today - january
    lecture = 0
    for i in range(delta.days + 1):
        lecture += random.randint(1, 25)
        day = january + td(days=i)
        Pricing.objects.create(day=day, price=random.uniform(0, 1))
        Lecture.objects.create(day=day, lecture=lecture)


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_auto_20160906_1916'),
    ]

    operations = [
        migrations.RunPython(fake_data_since_january),
    ]
