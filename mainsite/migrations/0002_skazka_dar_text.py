# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skazka_dar',
            name='text',
            field=models.TextField(default='123', max_length=2000),
        ),
    ]
