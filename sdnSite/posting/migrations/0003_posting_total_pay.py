# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-11 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0002_auto_20170410_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='total_pay',
            field=models.FloatField(default=100),
        ),
    ]
