from rest_framework.fields import ReadOnlyField, SerializerMethodField
from rest_framework import serializers
from django.urls import reverse

from blogs.models import Blog, Category, Post


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

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


def get_field_choices():
    return sorted([
        (cat.id, cat.cat_name) for cat in Category.objects.all()
    ])


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'blog', 'title', 'intro', 'body', 'image', 'date_time_pub', 'category']
        read_only_fields = ['id']
        depth = 1


class PostSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'blog', 'title', 'intro', 'body', 'image', 'date_time_pub', 'category']
        read_only_fields = ['id']


class PostWriteSerializer(PostListSerializer):

    categories = Category.objects.all()

    body = serializers.CharField()
    category = serializers.MultipleChoiceField(choices=categories)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
