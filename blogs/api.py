from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404

from blogs.models import Blog, Post
from blogs.permissions import PostPermission
from blogs.serializers import BlogListSerializer, PostListSerializer, PostWriteSerializer, PostSerializer, \
    PostSaveSerializer
from rest_framework.response import Response
from datetime import datetime


from blogs.views import PostUserList, PostListQuery


class BlogListApi(ListCreateAPIView):
    serializer_class = BlogListSerializer

    def get_queryset(self):
        if self.request.data.get('search'):
            query = Blog.objects.filter(title__contains=self.request.data.get('search'))
        else:
            query = Blog.objects.all()
        if self.request.data.get('order'):
            return query.order_by('owner__first_name')
        else:
            return query


class PostListModelView(PostListQuery, ListCreateAPIView):

    def get_serializer_class(self):
        return PostListSerializer


class PostListView(APIView):

    permission_classes = [PostPermission]

    def get(self, request, pk):
        blog_user_id = Blog.objects.filter(pk=pk).first()
        if request.user.id == blog_user_id.id:
            posts = Post.objects.filter(blog=pk).order_by('-date_time_pub')
        elif request.user.is_superuser:
            posts = Post.objects.filter(blog=pk).order_by('-date_time_pub')
        else:
            posts = Post.objects.filter(blog=pk, date_time_pub__lte=datetime.now()).order_by('-date_time_pub')

        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetailView(RetrieveUpdateDestroyAPIView):

    permission_classes = [PostPermission]

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostSaveView(CreateAPIView):

    permission_classes = [PostPermission]

    serializer_class = PostSaveSerializer

    def perform_create(self, serializer):
        serializer.save()


class PostListView2(ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [PostPermission]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        else:
            return PostSaveSerializer

    def post(self, request, *args, **kwargs):

        blog_own = Blog.objects.filter(id=request.data.get('blog')).first()
        temp = blog_own.owner
        if (temp == request.user) or request.user.is_superuser:
            return self.create(request, *args, **kwargs)
        else:
            error = {'error': 'action forbidden'}
            return Response(error, status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all().order_by('-date_time_pub')
        elif self.request.user.is_authenticated:
            return Post.objects.filter(Q(date_time_pub__lte=datetime.now()) | Q(blog__owner=self.request.user)).order_by('-date_time_pub')
        else:
            return Post.objects.filter(date_time_pub__lte=datetime.now()).order_by('-date_time_pub')
