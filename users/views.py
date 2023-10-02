from .serializers import UserSerializer, LoginUserSerializer
from .models import User
from rest_framework import viewsets, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response

from django.contrib.auth import login


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginUserViewSet(APIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return Response(
                {
                    "user": UserSerializer(user).data,
                    "message": "success",
                    "status": status.HTTP_200_OK,
                }
            )
        return Response(
            {
                "user": None,
                "message": "failed",
                "status": status.HTTP_400_BAD_REQUEST,
            }
        )
