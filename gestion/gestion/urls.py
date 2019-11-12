# -*- coding: utf-8 -*-
"""gestion URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from gestion import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')), 
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'', include('inicio.url', namespace='inicio')),
    url(r'', include('cuenta.url', namespace='cuenta')),
    url(r'', include('persona.url', namespace='persona')),
    url(r'', include('infraccion.url', namespace='infraccion')),

    #url para acceder a la imagenes que estan en la carpeta media del proyecto
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
