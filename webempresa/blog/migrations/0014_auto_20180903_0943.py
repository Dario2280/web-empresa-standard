# Generated by Django 2.0.2 on 2018-09-03 13:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20180901_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 3, 13, 43, 52, 720177, tzinfo=utc), verbose_name='fecha de publicacion'),
        ),
    ]
