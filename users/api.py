from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from users.serializers import UserRegisterSerializer, UserSerializer


class UserViewSet(APIView):

    def put(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            user_serializer = UserSerializer(new_user)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
