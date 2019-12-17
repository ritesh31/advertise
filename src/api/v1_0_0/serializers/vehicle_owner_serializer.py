from rest_framework import serializers
from django.db import transaction
from vehicleowner.models import VehicleOwner, Vehicle
from user.models import User
from api.v1_0_0.serializers.user_serializer import UserSerializer

class VehicleOwnerSerializer(serializers.ModelSerializer):
  class Meta:
    model = VehicleOwner
    fields = ('id', 'owner_name', 'address', 'zip_code', 'city', 'user', )

class CurrentUserDefault:
  """
  May be applied as a `default=...` value on a serializer field.
  Returns the current user.
  """
  requires_context = True

  def __call__(self, serializer_field):
    return serializer_field.context

class VehicleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vehicle
    fields = ('vehicle_number', 'vehicle_type', 'vehicle_owner')

class VehicleOwnerCreationSerializer(serializers.ModelSerializer):
  """
  Nested Serializer for Signup. If user is present get user object else create new
  """
  user = UserSerializer()
  class Meta:
    model = VehicleOwner
    fields = ('owner_name', 'address', 'zip_code', 'city', 'user', )

  @transaction.atomic
  def create(self, validated_data):
    user_data = validated_data.get('user')
    user, created = User.objects.get_or_create(email=user_data['email'], 
                                                defaults={'password':user_data['password']})
    if created:
      user.set_password(user_data['password'])
      user.save()
      validated_data['user'] = user
      vehicle_owner = super().create(validated_data)
      return vehicle_owner

