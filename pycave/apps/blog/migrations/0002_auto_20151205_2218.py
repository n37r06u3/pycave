# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-05 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
