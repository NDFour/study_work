# Generated by Django 2.2.5 on 2020-05-30 12:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('author', models.CharField(max_length=255, verbose_name='作者')),
                ('_type', models.CharField(max_length=255, verbose_name='类型')),
                ('body', models.TextField(verbose_name='正文')),
                ('prior', models.IntegerField(default=0, verbose_name='显示优先级')),
                ('display', models.BooleanField(default=False, verbose_name='是否发布')),
                ('article_views', models.PositiveIntegerField(default=0, verbose_name='阅读次数')),
                ('article_pub_date', models.DateTimeField(default=datetime.datetime(2020, 5, 30, 12, 38, 25, 905570, tzinfo=utc), verbose_name='更新时间')),
            ],
        ),
    ]
