# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postureapp', '0002_document_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repstatus', models.NullBooleanField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]