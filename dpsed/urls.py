"""eip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.dps_list),
    url(r'^create/$', views.dps_create),
    url(r'^detail/(?P<id>\d+)/$', views.dps_detail , name='detail'),
    url(r'^update/(?P<id>\d+)/$', views.dps_update, name='update'),
    url(r'^delete/(?P<id>\d+)/$', views.dps_delete),
]
