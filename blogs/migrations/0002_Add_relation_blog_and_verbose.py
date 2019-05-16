# Generated by Django 2.2.1 on 2019-05-13 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_first_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog', verbose_name='Blog'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.FilePathField(verbose_name='Imagen de cabecera'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Propietrio'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_time_pub',
            field=models.DateField(auto_now=True, verbose_name='Fecha de publicación'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FilePathField(verbose_name='Imagen de cabecera'),
        ),
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.TextField(max_length=200, verbose_name='Introducción'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]