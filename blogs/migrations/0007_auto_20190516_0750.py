# Generated by Django 2.2.1 on 2019-05-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20190516_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(path='C:\\Users\\basanta79\\Documents\\bootcamp\\07_py_django\\wordplease\\images', verbose_name='Imagen de cabecera'),
        ),
    ]
