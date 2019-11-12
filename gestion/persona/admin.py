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

from __future__ import unicode_literals
from django.contrib import admin
from .models import Persona


"""Permite administrar la visualización de los datos de Persona en la base de datos del
	sitio de administración"""
class AdminPersona(admin.ModelAdmin):
	"""Permite establecer la información de los datos id, user, identificacion, telefono, 
	direccion empresa, cargolaboral, estado, tipo, descripciontu, imagen y thumbnail del 
	modelo Persona que se mostrarán en el sitio de administración"""
	list_display = ('id', 'user', 'identificacion', 'sede', 'cargo', 'tipo', 'imagen','thumbnail',)
	
	"""Permite establecer el parametro de busqueda identificacion de la tabla Persona 
	en el sitio de administración"""
	search_fields = ('identificacion',)

#Permite registrar las clases Usuario y AdminUsuario
admin.site.register(Persona, AdminPersona)