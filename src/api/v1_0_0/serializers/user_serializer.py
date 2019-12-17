from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from user.models import User
from advertiser.models import Advertiser

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('email', 'password',)

class UserLoginSerializer(serializers.ModelSerializer):
  """
    User Authentication Serializer
  """
  email = serializers.EmailField(required=True, allow_blank=False)

  class Meta:
    model = User
    fields = ('email', 'password')
    extra_kwargs = {
      'password': {
        'write_only': True
      }
    }

  def validate(self, data):
    """
    User Authentication
    """
    user = authenticate(email=data['email'], password=data['password'])
    if not user:
      raise AuthenticationFailed(error='Invalid credentials')
    return user


