from django.shortcuts import render
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated

from knox.auth import TokenAuthentication
from api.v1_0_0.permissions.user_permissions import UserPermissions
from advertiser.models import Advertiser, Advertise, Document
from api.v1_0_0.serializers.advertiser_serializer import AdvertiserSerializer, AdvertiserCreationSerializer, AdvertiseSerializer, AdvertiseCreationSerializer, DocumentSerializer

class AdvertiserView(viewsets.ModelViewSet):
    """
    A simple ViewSet for creating Advertiser objects.
    """
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (UserPermissions,)

    def get_serializer_class(self):
        if self.action == 'create':
            return AdvertiserCreationSerializer
        return AdvertiserSerializer

class AdvertiseView(viewsets.ModelViewSet):
    """
    A simple ViewSet for creating Advertise objects.
    """
    queryset = Advertise.objects.all()
    serializer_class = AdvertiseSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (UserPermissions,)

    def get_serializer_class(self):
        if self.action == 'create':
            return AdvertiseCreationSerializer
        return AdvertiseSerializer

    def perform_create(self, serializer):
        serializer.validated_data['advertiser'] = self.request.user.advertiser
        serializer.save()


    def get_queryset(self):
        if self.request.user.is_superuser:
            return Advertise.objects.all()
        return Advertise.objects.filter(advertiser=self.request.user.advertiser)

class DocumentView(KnoxLoginView):
    """
    A simple ViewSet for creating document objects.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer