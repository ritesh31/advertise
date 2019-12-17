from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import (UserView, AdvertiserView, AdvertiseView, DocumentView, VehicleOwnerView, VehicleView)
# CategoryViewSet, VendorViewSet, CompanyViewSet, InvoiceViewSet, DocumentViewSet, StateChoiceView)

router = routers.DefaultRouter()
router.register(r'user', UserView)
router.register(r'advertiser', AdvertiserView, base_name='advertiser')
router.register(r'vehicleowner', VehicleOwnerView, base_name='vehicleowner')
router.register(r'vehicle', VehicleView, base_name='vehicle')
router.register(r'advertise', AdvertiseView, base_name='advertise')

urlpatterns = [
    path('', include(router.urls)),
]
