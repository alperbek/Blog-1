# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 16:26
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
