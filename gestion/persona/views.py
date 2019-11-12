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
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from inicio.mixins import LoginRequiredMixin
from .models import Persona
from django.core.urlresolvers import reverse, reverse_lazy


"""ListView: Vista que permite mostrar un listado de cualquier objeto existente"""
class PersonaListView(LoginRequiredMixin, ListView):
	"""Permite listar todas las Personas de la base de datos"""
	
	model = Persona
	context_object_name = 'personas'
	template_name = 'persona/persona_list.html'

	def get_context_data(self,**kwargs):
		"""Permite devolver un diccionario que representa el contexto de la plantilla"""

		context = super(PersonaListView,self).get_context_data(**kwargs)
		return context

"""DetailView: Vista que contiene el objeto sobre el que está operando la vista"""
class PersonaDetailView(LoginRequiredMixin, DetailView):
	"""Permite mientras se ejecuta contener el objeto persona sobre el que se esta 
	operando la vista"""
	
	model = Persona
	context_object_name = 'persona'
	template_name = 'persona/detalle.html'