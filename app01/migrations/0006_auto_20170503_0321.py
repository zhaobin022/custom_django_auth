# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 03:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_groupprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupprofile',
            name='group',
        ),
        migrations.DeleteModel(
            name='GroupProfile',
        ),
    ]
