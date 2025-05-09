"""
URL configuration for festival_planner project.

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
from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

import artists.views
import mails.views

router.register(r'artists',
                artists.views.ArtistViewSet,
                basename='artists')

router.register(r'mails',
                mails.views.MailViewSet,
                basename='mails')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/', include((router.urls, 'api')))
]

admin.site.site_url = '/api/'

from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView, SpectacularSwaggerView)

urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger-doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('doc/', SpectacularRedocView.as_view(url_name='schema'), name='doc'),
]
