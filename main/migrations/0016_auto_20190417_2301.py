# Generated by Django 2.1.8 on 2019-04-17 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190417_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coments',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 17, 23, 1, 53, 89623), verbose_name='Дата комментария'),
        ),
    ]
