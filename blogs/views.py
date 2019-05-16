from django.shortcuts import render
from django.views.generic import ListView

from blogs.models import Blog, Post


class PostList(ListView):

    template_name = 'blogs/post_list.html'

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-date_time_pub')
        return queryset
