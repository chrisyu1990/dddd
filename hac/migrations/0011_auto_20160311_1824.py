# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-11 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hac', '0010_auto_20160224_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='imageUrl',
            field=models.ImageField(default='exit', upload_to=''),
            preserve_default=False,
        ),
    ]
