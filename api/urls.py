"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.gis import admin
from rest_framework import routers, serializers, viewsets
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from api import views

urlpatterns = [
    url(r'^household/', views.householddetail),
#    url(r'^householdaudio/', views.hadetail),
#    url(r'^householdphoto/', views.hpdetail),
#    url(r'^householdvideo/', views.hvdetail),
    url(r'^farm/', views.farmdetail),
#    url(r'^farmphoto/', views.fpdetail),
#    url(r'^farmvideo/', views.fvdetail),
    url(r'^crop/', views.cropdetail),
    url(r'^well/', views.welldetail),
    url(r'^yield/', views.yielddetail),
#    url(r'^wellphoto/', views.wpdetail),
    url(r'^member/', views.memberdetail),
    url(r'^season/', views.seasondetail),
    url(r'^storage/', views.storagedetail),
#    url(r'^storagephoto/', views.spdetail),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)