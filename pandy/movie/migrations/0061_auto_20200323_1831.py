# Generated by Django 2.2.5 on 2020-03-23 10:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0060_auto_20200323_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='v_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 23, 10, 31, 55, 382560, tzinfo=utc), verbose_name='最后更新时间'),
        ),
    ]