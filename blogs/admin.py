from django.contrib import admin
from blogs.models import Category, Blog, Post


admin.site.site_header = "wordplease Admin"
admin.site.site_title = "wordplease Admin Portal"
admin.site.index_title = "Welcome to wordplease Portal"

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Post)


