# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
