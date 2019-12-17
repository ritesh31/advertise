from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, )
from user.models import User
# from utils.mixins.models import BaseModelMixins

class VehicleOwner(models.Model):
  """
  Class implementing a fully featured User model with
  admin-compliant permissions.
  Email, password and vehicle number are required. Other fields are optional.

  """
  owner_name = models.CharField(_('Owner Name'), max_length=255, null=False)
  address = models.TextField(_('Address'))
  zip_code = models.CharField(_('Zip'), max_length=128)
  city = models.CharField(_('City'), max_length=128, db_index=True, blank=True, null=True)
  date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
  # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vehicle_owner')

class Vehicle(models.Model):
  """
  Class implementing a fully featured User model with
  admin-compliant permissions.

  """
  vehicle_number = models.CharField(_('Vehicle Number'), max_length=15, unique=True, null=False)
  vehicle_type = models.CharField(_('Doc Type'), max_length=15, null=False)
  vehicle_owner = models.ForeignKey(VehicleOwner, on_delete=models.CASCADE, related_name='vehicles')
