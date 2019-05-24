from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from datetime import datetime

from django.db.models import ManyToManyField


class Category(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name="Categoria")

    def __str__(self):
        return self.cat_name


class Blog(models.Model):
    owner = models.ForeignKey(User,verbose_name="Propietrio", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Título", max_length=50)
    blog_image = models.URLField(null=True, verbose_name="Imagen de cabecera")

    def __str__(self):
        return '{0} -> {1}'.format(self.owner, self.title)


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Blog", default=None)
    title = models.CharField(verbose_name="Título",  max_length=100)
    intro = models.TextField(verbose_name="Introducción", max_length=200)
    body = models.TextField(verbose_name="Contenido")
    image = models.URLField(verbose_name="Imagen de cabecera")
    date_time_pub = models.DateField(verbose_name="Fecha de publicación", default=datetime.now)
    category = models.ManyToManyField(Category, verbose_name="Categoria")

    def __str__(self):
        return '{0} -> {1}'.format(self.blog, self.title)
