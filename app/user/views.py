"""
viewes for the user api
"""
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """create a new user in the systems"""
    serializer_class = UserSerializer
