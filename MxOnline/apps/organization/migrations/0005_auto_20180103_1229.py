# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_arg',
            field=models.IntegerField(default=20, max_length=3, verbose_name='讲师年龄'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_td',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='教学特点'),
        ),
    ]
