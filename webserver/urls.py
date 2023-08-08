"""
URL configuration for webserver project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account.views import (
    registration_view,
    logoutview,
    loginview,
    must_authenticate_view,
    must_be_staff,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('folkszoglet.urls')),
    path('regisztracio/', registration_view, name='register'),
    path('video/',include ('video.urls', 'video')),
    path('logout/',logoutview, name='logout'),
    path('bejelentkezes/',loginview, name='login'),
    path('hitelesites_szukseges/',must_authenticate_view, name='hitelesites_szukseges'),
    path('nincs_jogosultsag/',must_be_staff, name='nincs_jogosultsag'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)