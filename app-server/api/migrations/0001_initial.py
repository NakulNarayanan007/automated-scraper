# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-04 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auto_scraper',
            fields=[
                ('url_id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('data', models.TextField(max_length=50000)),
            ],
        ),
        migrations.CreateModel(
            name='url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_link', models.CharField(max_length=300)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]
