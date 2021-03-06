# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_skazka_dar_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='risunki',
            fields=[
                ('id_risunok', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/img/risunki')),
                ('author', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Рисунок',
                'verbose_name_plural': 'Рисунки',
            },
        ),
    ]
