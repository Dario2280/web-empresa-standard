# Generated by Django 2.0.2 on 2018-08-30 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180830_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 30, 18, 53, 56, 792311, tzinfo=utc), verbose_name='fecha de publicacion'),
        ),
    ]
