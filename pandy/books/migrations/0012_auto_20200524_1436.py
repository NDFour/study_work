# Generated by Django 2.2.5 on 2020-05-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20200524_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_pub_date',
            field=models.DateTimeField(verbose_name='更新时间'),
        ),
    ]