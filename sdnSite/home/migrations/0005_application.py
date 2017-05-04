# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-30 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170330_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('app_id', models.IntegerField(primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cover_letter', models.CharField(max_length=1000)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Posting')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Member')),
                ('resume_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.File')),
            ],
        ),
    ]
