# Generated by Django 2.0.2 on 2018-09-01 15:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180901_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 15, 59, 20, 787420, tzinfo=utc), verbose_name='fecha de publicacion'),
        ),
    ]
