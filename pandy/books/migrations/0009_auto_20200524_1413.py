# Generated by Django 2.2.5 on 2020-05-24 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20200323_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 24, 14, 13, 22, 766330), verbose_name='更新时间'),
        ),
    ]