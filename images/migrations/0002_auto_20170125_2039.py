# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-25 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d'),
        ),
    ]
