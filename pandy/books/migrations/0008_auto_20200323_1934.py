# Generated by Django 2.2 on 2020-03-23 11:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200323_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 23, 11, 34, 38, 373367, tzinfo=utc), verbose_name='更新时间'),
        ),
    ]