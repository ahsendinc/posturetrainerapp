# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('postureapp', '0003_recommendation'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickleObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('args', picklefield.fields.PickledObjectField(editable=False)),
            ],
        ),
    ]
