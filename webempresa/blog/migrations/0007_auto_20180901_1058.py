# Generated by Django 2.0.2 on 2018-09-01 14:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180901_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 14, 58, 30, 882341, tzinfo=utc), verbose_name='fecha de publicacion'),
        ),
    ]
