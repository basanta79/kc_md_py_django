# Generated by Django 2.2.1 on 2019-05-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_remove_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(path='/images/', verbose_name='Imagen de cabecera'),
        ),
    ]
