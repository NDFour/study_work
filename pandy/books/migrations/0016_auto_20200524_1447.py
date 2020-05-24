# Generated by Django 2.2.5 on 2020-05-24 06:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20200524_1442'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book_notify',
        ),
        migrations.AlterField(
            model_name='books',
            name='book_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 6, 47, 38, 905474, tzinfo=utc), verbose_name='更新时间'),
        ),
    ]