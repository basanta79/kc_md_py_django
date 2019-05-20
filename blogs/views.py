from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blogs.models import Blog, Post
from datetime import datetime


class PostList(ListView):

    template_name = 'blogs/post_list.html'

    def get_queryset(self):
        queryset = Post.objects.filter(date_time_pub__lte=datetime.now()).order_by('-date_time_pub')
        return queryset


class BlogList(ListView):

    template_name = 'blog/blog_list.html'

    def get_queryset(self):
        queryset = Blog.objects.all()
        return queryset


class PostUserList(ListView):

    template_name = 'blogs/post_list.html'

    def get_queryset(self):
        print(self.kwargs.get('usr'))
        queryset = Post.objects.filter(date_time_pub__lte=datetime.now(), blog__owner__username=self.kwargs.get('usr')).order_by('-date_time_pub')
        return queryset


class PostDetail(DetailView):

    template_name = 'blogs/post_detail.html'

    def get_queryset(self):
        queryset = Post.objects.filter(
            pk=self.kwargs.get('pk'),
            date_time_pub__lte=datetime.now(),
            blog__owner__username=self.kwargs.get('usr')
        )
        return queryset
