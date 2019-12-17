from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User

class UserAdmin(admin.ModelAdmin):
  """
  User Admin
  """
  model = User
  readonly_fields = ('id',)
  search_fields = ('email',)
  
admin.site.register(User, UserAdmin)
