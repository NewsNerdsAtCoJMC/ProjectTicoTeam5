# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0006_merge_20170420_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areacrime',
            name='school',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='school',
        ),
        migrations.AlterField(
            model_name='activities',
            name='state_ranking',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='AreaCrime',
        ),
        migrations.DeleteModel(
            name='Funding',
        ),
    ]
