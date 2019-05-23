from rest_framework.fields import ReadOnlyField, SerializerMethodField
from rest_framework.serializers import ModelSerializer
from django.urls import reverse

from blogs.models import Blog


class BlogListSerializer(ModelSerializer):

    username = ReadOnlyField(source='owner.username')
    url = SerializerMethodField()

    def get_url(self, obj):
        return reverse('home') + str(obj.owner)

    class Meta:
        model = Blog
        fields = ['title', 'owner', 'username', 'url']
