from django.shortcuts import render
from django.contrib.auth import login
from rest_framework.permissions import (
    AllowAny
)
from knox.views import LoginView as KnoxLoginView
from rest_framework import (viewsets, views, decorators)

from user.models import User
from api.v1_0_0.serializers.user_serializer import UserSerializer, UserLoginSerializer

class UserView(viewsets.ModelViewSet):
    """
    An endpoint for user.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserLoginView(viewsets.ModelViewSet):
    """
    An endpoint for user login.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return KnoxLoginView().post(request, format=None)
