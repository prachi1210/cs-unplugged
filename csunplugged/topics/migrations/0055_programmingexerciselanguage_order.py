# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0054_lesson_classroom_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmingexerciselanguage',
            name='order',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
