# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-31 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_courseorg_xxrs'),
        ('courses', '0002_auto_20171228_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='coures',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='课程机构'),
        ),
    ]
