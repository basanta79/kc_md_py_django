from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog, Post
from blogs.permissions import PostPermission
from blogs.serializers import BlogListSerializer, PostListSerializer
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
        if request.user.is_authenticated:
            posts = Post.objects.filter(blog=pk)
        else:
            posts = Post.objects.filter(blog=pk, date_time_pub__lte=datetime.now()).order_by('-date_time_pub')

        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)



