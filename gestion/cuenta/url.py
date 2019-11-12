# -*- coding: utf-8 -*-

########################################################################################
#Módulo: Gestionar Personal 
#Autor: Leidy Johanna Carvajal Ortiz
#Fecha: 2017/01/10
#Versión: 1.0
#
#Descripción: Este módulo permite identificar los roles(Administrador, Interventor y 
# Recaudador) del sistema, mostrar la sesión y recuperar la contraseña  de la cuenta 		 			  
#			  
########################################################################################

from django.conf.urls import include, url
from .views import Editar
from .views import EditarContrasenia
from .views import Perfil

"""Define las direcciones web o url de la aplicación Cuenta"""
urlpatterns = [
	url(r'^cuenta/editar$', Editar.as_view(), name='editar'),
	url(r'^cuenta/editar_contrasenia$', EditarContrasenia.as_view(), name='editar_contrasenia'),
	url(r'^cuenta/perfil$', Perfil.as_view(), name='perfil'),
]