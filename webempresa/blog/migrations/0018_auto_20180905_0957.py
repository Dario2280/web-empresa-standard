# Generated by Django 2.0.2 on 2018-09-05 13:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20180905_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 5, 13, 57, 50, 344926, tzinfo=utc), verbose_name='fecha de publicacion'),
        ),
    ]
