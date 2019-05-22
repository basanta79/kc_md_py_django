from rest_framework.generics import ListCreateAPIView

from blogs.models import Blog
from blogs.serializers import BlogListSerializer


class BlogListApi(ListCreateAPIView):
    serializer_class = BlogListSerializer

    def get_queryset(self):
        if self.request.data.get('order'):
            return Blog.objects.filter(title__contains='').order_by('owner__first_name')
        else:
            return Blog.objects.all()



