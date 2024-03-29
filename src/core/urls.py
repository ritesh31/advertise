"""advertise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from knox import views as knox_views
from api.v1_0_0.views.user_view import UserView, UserLoginView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('user', UserView, base_name='user')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('login/', UserLoginView.as_view({'get': 'list'}), name='login'),
]
