# Generated by Django 2.1 on 2018-08-19 03:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0018_auto_20180813_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='v_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 19, 3, 57, 52, 785480, tzinfo=utc), verbose_name='最后更新时间'),
        ),
    ]