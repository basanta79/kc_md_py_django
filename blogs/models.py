from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=50)


class Blog(models.Model):
    owner = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    blog_image = models.FilePathField()



class Post(models.Model):
    title = models.CharField(max_length=100)
    intro = models.TextField(max_length=200)
    body = models.TextField()
    image = models.FilePathField()
    date_time_pub = models.DateField(auto_now=True)
    category = models.IntegerField()