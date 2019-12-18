from django.shortcuts import render
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from api.v1_0_0.permissions.user_permissions import UserPermissions

from vehicleowner.models import VehicleOwner, Vehicle
from api.v1_0_0.serializers.vehicle_owner_serializer import VehicleOwnerSerializer, VehicleOwnerCreationSerializer, VehicleSerializer

class VehicleOwnerView(viewsets.ModelViewSet):
    """
    A simple ViewSet for creating Vehicle Owner objects.
    """
    queryset = VehicleOwner.objects.all()
    serializer_class = VehicleOwnerSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (UserPermissions,)

    def get_serializer_class(self):
        if self.action == 'create':
            return VehicleOwnerCreationSerializer
        return VehicleOwnerSerializer

class VehicleView(viewsets.ModelViewSet):
    """
    An endpoint for Vehicle.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (UserPermissions,)

    def perform_create(self, serializer):
        serializer.validated_data['vehicle_owner'] = self.request.user.vehicle_owner
        serializer.save()

    def get_queryset(self):
        if self.request.user.is_superuser:
           return Vehicle.objects.all()
        return Vehicle.objects.filter(vehicle_owner=self.request.user.vehicle_owner)