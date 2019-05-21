# Generated by Django 2.2.1 on 2019-05-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_blog_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blogs.Category', verbose_name='Categoria'),
        ),
    ]