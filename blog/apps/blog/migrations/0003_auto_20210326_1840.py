# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2021-03-26 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210326_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(default='描述就是没有描述...', help_text='用来作为SEO中description,长度参考SEO标准', max_length=240, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(default='描述就是没有描述...', help_text='用来作为SEO中description,长度参考SEO标准', max_length=240, verbose_name='描述'),
        ),
    ]
