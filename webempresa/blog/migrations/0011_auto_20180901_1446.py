# Generated by Django 2.0.2 on 2018-09-01 18:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180901_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 18, 46, 16, 354830, tzinfo=utc), verbose_name='fecha de publicacion'),
        ),
    ]
