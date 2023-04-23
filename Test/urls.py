"""
URL configuration for Test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from shops.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('city/', CityListView.as_view(), name='city-list'),
    path('city/<int:city_id>/street', StreetListView.as_view(), name='street-list'),
    path('shop/', ShopListView.as_view(), name='shop-list-create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


