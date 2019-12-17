from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from user.models import User
from vehicleowner.models import VehicleOwner

class Advertiser(models.Model):
  """
  Class implementing a fully featured User model with
  admin-compliant permissions.
  Email, password and vehicle number are required. Other fields are optional.

  """
  name = models.CharField(_('Name'), max_length=255, null=False)
  address = models.TextField(_('Address'), blank=True, null=True)
  zip_code = models.CharField(_('Zipcode'), max_length=128)
  city = models.CharField(_('City'), max_length=128, db_index=True)
  date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
  # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='advertiser')

class Document(models.Model):
  """
  Class implementing a fully featured User model with
  admin-compliant permissions.

  """
  presigned_url = models.CharField(_('Presigned Url'), max_length=255, null=False, unique=False)
  size = models.IntegerField(_('Size'))
  doc_type = models.CharField(_('Doc Type'), max_length=15, null=False)
 
class Advertise(models.Model):
  """
  Class implementing a fully featured User model with
  admin-compliant permissions.

  """
  price = models.FloatField(_('Price'))
  description = models.TextField(_('Description'))
  document_file = models.OneToOneField(Document, on_delete=models.CASCADE)
  vehicle_owner = models.OneToOneField(VehicleOwner, on_delete=models.CASCADE)
  advertiser = models.OneToOneField(Advertiser, on_delete=models.CASCADE)

