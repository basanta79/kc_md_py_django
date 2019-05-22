from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView

from blogs.forms import CreatePostForm
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


class CreatePost(LoginRequiredMixin, FormView):
    template_name = 'blogs/create_post.html'
    form_class = CreatePostForm
    success_url = 'login'

    def get_form(self, form_class=None):
        form = super(CreatePost, self).get_form(form_class)  # instantiate using parent
        form.fields['blog'].queryset = Blog.objects.filter(owner=self.request.user)
        return form

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
