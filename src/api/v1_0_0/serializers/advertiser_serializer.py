from rest_framework import serializers
from django.db import transaction
from advertiser.models import Advertiser, Advertise, Document
from user.models import User
from api.v1_0_0.serializers.user_serializer import UserSerializer

class DocumentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Document
    fields = ('presigned_url', 'size', 'doc_type', )

class AdvertiserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Advertiser
    fields = ('id', 'name', 'address', 'zip_code', 'city', )

class AdvertiseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Advertise
    fields = ('id', 'price', 'description', 'document_file', 'vehicle_owner', 'advertiser')

class AdvertiseCreationSerializer(serializers.ModelSerializer):
  """
  Nested Serializer for document creation.
  """
  document_file = DocumentSerializer()
  class Meta:
    model = Advertise
    fields = ('price', 'description', 'document_file', 'vehicle_owner',)

  @transaction.atomic
  def create(self, validated_data):
    document_data = validated_data.get('document_file')
    document, uploaded_doc = Document.objects.get_or_create(presigned_url = document_data['presigned_url'], 
                                                            size = document_data['size'], 
                                                            doc_type = document_data['doc_type'])
    if document:
      document.save()
    validated_data['document_file'] = document
    advertise = super().create(validated_data)
    return advertise

class AdvertiserCreationSerializer(serializers.ModelSerializer):
  """
  Nested Serializer for Signup. If user is present get user object else create new
  """
  user = UserSerializer()
  class Meta:
    model = Advertiser
    fields = ('id', 'name', 'address', 'zip_code', 'city', 'user', )
    read_only_fields = ('id',)

  @transaction.atomic
  def create(self, validated_data):
      user_data = validated_data.get('user')
      user, created = User.objects.get_or_create(email=user_data['email'],
                                                  defaults={'password':user_data['password']})
      if created:
        user.set_password(user_data['password'])
        user.save()
      validated_data['user'] = user
      advertiser = super().create(validated_data)
      return advertiser

