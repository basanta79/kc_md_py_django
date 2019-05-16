from django.shortcuts import render
from django.views import View, ListView

from blogs.models import Blog, Post


class BlogList(ListView):

    template_name = 'blogs/post_list.html'

    def get_queryset(self):
        queryset = Post.objects.all().order_by('date_time_pub')
        return queryset
