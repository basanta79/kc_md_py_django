from django.contrib import admin
from blogs.models import Category, Blog, Post


# Register your models here.
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Post)
