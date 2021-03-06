# Generated by Django 2.0.2 on 2018-08-30 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titulo')),
                ('subtitle', models.CharField(max_length=200, verbose_name='subtitulo')),
                ('content', models.TextField(verbose_name='contenido')),
                ('image', models.ImageField(upload_to='services', verbose_name='imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
                'ordering': ['-created'],
            },
        ),
    ]
