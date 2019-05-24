from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers


class UserListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserSerializer(UserListSerializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    date_joined = serializers.ReadOnlyField()


class UserRegisterSerializer(UserSerializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def create(self, validated_data):
        user = User()
        return self.update(user, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.set_password(validated_data.get('password'))
        instance.email = validated_data.get('email')
        instance.save()
        return instance
