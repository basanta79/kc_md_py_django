from django.forms import ModelForm

from blogs.models import Post, Blog


class CreatePostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['blog', 'title', 'intro', 'body', 'image', 'date_time_pub', 'category']