# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-19 03:48
from __future__ import unicode_literals

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('pwd', user.models.CCharField(max_length=20)),
            ],
        ),
    ]
