from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, )
from django.contrib.auth.models import PermissionsMixin

# from utils.mixins.models import BaseModelMixins
from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
  """
  Class implementing a fully featured User model with
  admin-compliant permissions.
  Email, password and vehicle number are required. Other fields are optional.

  """
  email = models.EmailField(_('Email Address'), max_length=255, unique=True, null=False)
  is_superuser = models.BooleanField(_('Superuser'), default=False)
  is_staff = models.BooleanField(_('Staff'), default=False)
  is_advertiser = models.BooleanField(_('Advertiser'), default=False)
  date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = [] # Email & Password are required by default.