# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postureapp', '0004_pickleobject'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickleobject',
            name='name',
            field=models.CharField(default='data', max_length=200),
            preserve_default=False,
        ),
    ]
