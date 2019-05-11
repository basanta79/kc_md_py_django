from django.db import models

# Create your models here.

class Blog(models.Model):
    owner = models.CharField(max_length=100)
    title = models.CharField(max_length=50)

    pass