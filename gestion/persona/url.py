# -*- coding: utf-8 -*-

########################################################################################
#Módulo: Gestionar Personal 
#Autor: Leidy Johanna Carvajal Ortiz
#Fecha: 2017/01/10
#Versión: 1.0
#
#Descripción: Este modulo permite al usuario administrador listar, crear, modificar y 
#			  eliminar el personal en la base de datos
#			  
########################################################################################

from django.conf.urls import include, url
from . import views
from . import forms

"""Define las direcciones web o url de la aplicación Persona"""
urlpatterns = [
    url(r'^persona/crear$', forms.PersonaCreateView.as_view(), name='crear'),
    url(r'^persona/actualizar/(?P<epk>\d+)/$', forms.PersonaUpdateView.as_view(), name='actualizar'),
    url(r'^persona/listado$', views.PersonaListView.as_view(), name='listar-personas'),
    url(r'^persona(?P<pk>\d+)/detalle/$', views.PersonaDetailView.as_view(), name='detalle'),
    url(r'^persona/eliminar/(?P<pk>\d+)/$', forms.PersonaDeleteView.as_view(), name='eliminar'),

]