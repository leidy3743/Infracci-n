# -*- encoding: utf-8 -*-

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, Adjust


class Infraccion(models.Model):
	"""Define el modelo de datos para infraccion"""

	#Número de identificación
	numero = models.CharField(max_length=20, verbose_name= ('Número de Identificación'))
	#Sede
	sede = models.CharField(max_length=100)
	#Descripción
	descripcion = models.TextField(verbose_name= ('Descripción'), null=True)
	#Placa asociada
	placa = models.CharField(max_length=6)
	#Fecha
	fecha = models.DateField()


	#Permite determinar una representacion en string del objeto infraccion
	def __str__(self):
		return self.sede

	#Permite determinar una representacion en string para el objeto (Esto es para versiones de Python 2)
	def __unicode__(self):
		return self.sede

	#Permite hacer modificaciones agregadas a la representacion del modelo
	class Meta:
		ordering = ['sede']
		verbose_name_plural = "Infracciones"
