"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blogs.api import BlogListApi, PostListView, PostListModelView, PostDetailView, PostListView2, PostSaveView
from blogs.views import PostList, BlogList, PostUserList, PostDetail, CreatePost
from users.api import UserViewSet, UserDetailViewSet
from users.views import Login, Logout, Signup

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('', PostList.as_view(), name='home'),
    path('blogs/', BlogList.as_view(), name='blog_list'),
    path('blogs/<str:usr>/', PostUserList.as_view(), name='blog_user_list'),
    path('blogs/<str:usr>/<int:pk>', PostDetail.as_view(), name='blog_post_detail'),

    path('new-post', CreatePost.as_view(), name='new-post'),

    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('signup', Signup.as_view(), name='signup'),

    path('api/v1/blogs/', BlogListApi.as_view(), name='api-blogs-list'),
    path('api/v1/user/', UserViewSet.as_view(), name='api-user-reg'),
    path('api/v1/user/<int:pk>', UserDetailViewSet.as_view(), name='api-user-detail'),

    path('api/v1/blog/<int:pk>', PostListView.as_view(), name='api-post-list'),
    path('api/v1/post/', PostListView2.as_view(), name='api-post-save'),
    path('api/v1/post/<int:pk>', PostDetailView.as_view(), name='api-post-detail')

]
