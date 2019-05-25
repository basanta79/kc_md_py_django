from rest_framework.permissions import BasePermission
from django.utils import timezone
import datetime


class PostPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user.is_superuser) or (request.user == obj.blog.owner) or (obj.date_time_pub <= datetime.date.today())

