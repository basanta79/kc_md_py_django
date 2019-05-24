from rest_framework.fields import ReadOnlyField, SerializerMethodField
from rest_framework import serializers
from django.urls import reverse

from blogs.models import Blog


class BlogListSerializer(serializers.ModelSerializer):

    username = ReadOnlyField(source='owner.username')
    url = SerializerMethodField()

    def get_url(self, obj):
        return reverse('home') + str(obj.owner)

    class Meta:
        model = Blog
        fields = ['title', 'owner', 'username', 'url']


class PostListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    image = serializers.URLField()
    intro = serializers.CharField()
    date_time_pub = serializers.DateField()
