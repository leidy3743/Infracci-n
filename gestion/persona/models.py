#!/usr/bin/env python
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

from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Adjust
from django.core.validators import EmailValidator


#Tipo de usuarios
USUARIO = 'Usuario'
ADMINISTRADOR = 'Administrador'


tipo_usuario = (
	(USUARIO, 'Usuario'),
	(ADMINISTRADOR, 'Administrador'),
)

#Django por defecto, cuando los modelos no tienen primary_key, coloca una llamada "id"
"""Model: Define la estructura de la tabla Persona en base de datos"""
class Persona(models.Model):
	"""Permite definir un listado de Personas"""

	#Login o user de la persona
	user = models.OneToOneField(User, related_name='persona', default=None, null=True, on_delete=models.CASCADE, db_index=True)
	#Indentificación de la persona, debe ser única
	identificacion = models.CharField(max_length=20, unique=True, help_text="Indentificacion de la persona, debe ser unica")
	#Dirección de residencia de la persona
	sede = models.CharField(max_length=200)
	#Cargo laboral de la persona
	cargo = models.CharField(max_length=200)
	#Tipos de usuarios que se puden crear
	tipo = models.CharField(max_length=50, choices=tipo_usuario, default=USUARIO)
	#Imagen o foto de perfil de la persona
	imagen = models.ImageField(upload_to = "imagenes/persona")
	#Thumbnail, que permite reducir la imagen del usuario
	thumbnail = ImageSpecField(source='imagen',
									  processors=[ResizeToFill(100, 50)],
									  format='JPEG',
									  options={'quality': 60})

	"""Permite ordenar la lista de personas por identificacion y asignarle el nombre en 
	plural"""
	class Meta:
		ordering = ['identificacion']
		verbose_name_plural = "Personas"

	#Permite determinar una representación en string del objeto Persona
	def __str__(self):
		return self.user.first_name + " " + self.user.last_name

	"""Permite determinar una representación en string para el objeto Persona (Para 
	versiones de Python 2)"""
	def __unicode__(self):
		return self.user.first_name + " " + self.user.last_name
		