# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 07:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_resource_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='thumbnail',
            new_name='thumbnail_static_path',
        ),
    ]