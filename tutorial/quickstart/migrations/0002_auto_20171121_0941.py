# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assignee',
            field=models.CharField(blank=True, max_length=90),
        ),
    ]