# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mygroup',
            name='permissions',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.DeleteModel(
            name='MyGroup',
        ),
    ]
