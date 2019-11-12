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

from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import UserUpdateForm
from .forms import UserPasswordUpdateForm
from .forms import PersonaUpdateForm
from persona.models import Persona
from inicio.mixins import LoginRequiredMixin

"""TemplateView:Presenta una plantilla determinada, con el contexto que contiene los 
parámetros capturados en la URL"""
class Perfil(LoginRequiredMixin, TemplateView):
	"""Permite mostrar el perfil de usuario"""
	def get(self,request,*args,**kwargs):
		"""Permite mostrar la vista de inicio"""
		return HttpResponseRedirect(reverse('inicio:login'))
		

class EditarContrasenia(LoginRequiredMixin, TemplateView):
	"""Permite modificar la contraseña del usuario"""

	def post(self,request,*args,**kwargs):
		""" Permite validar si la contraseña coincide con el usuario, si es así, guarda 
		los datos de lo contrario muestra un mensaje de error retornando el formulario 
		para editar la contraseña, señalando los campos con error """
		user_form = UserUpdateForm(instance=request.user)
		persona_form = PersonaUpdateForm(instance=request.user.persona)
		user_password_update_form = UserPasswordUpdateForm(user=request.user,data=request.POST)

		if user_password_update_form.is_valid():
			user_password_update_form.save()
			return HttpResponseRedirect(reverse('inicio:login'))
		else:
			messages.error(request,'Hay errores en algun campo')
			context = {
			'user_form':user_form,
			'persona_form':persona_form,
			'user_password_update_form':user_password_update_form
			}
			return render(request, 'cuenta/editar.html', context)


class Editar(LoginRequiredMixin, TemplateView):
	"""Permite modificar los datos de la cuenta de usuario (User, Persona)"""

	def get(self,request,*args,**kwargs):
		"""Permite mostrar el formulario para actualizar los datos de la cuenta de 
		usuario"""
		user_form = UserUpdateForm(instance=request.user)
		persona_form = PersonaUpdateForm(instance=request.user.persona)
		user_password_update_form = UserPasswordUpdateForm(user=request.user)

		context = {
		'user_form':user_form,
		'persona_form':persona_form,
		'user_password_update_form':user_password_update_form
		}
		return render(request, 'cuenta/editar.html', context)

	def post(self,request,*args,**kwargs):
		"""Permite determinar si los datos del formulario son validos para enviarlos, 
		sino retorna el formulario con los campos de error"""
		user_form = UserUpdateForm(request.POST,instance=request.user)
		persona_form = PersonaUpdateForm(request.POST,request.FILES,instance=request.user.persona)

		if user_form.is_valid() and persona_form.is_valid():
			user_form.save()
			persona_form.save()

			messages.info(request,'Tu cuenta ha sido modificada con exito')
			context = {}
			return HttpResponseRedirect(reverse('inicio:login'))

		else:
			user_form = UserUpdateForm(request.POST,instance=request.user)
			persona_form = PersonaUpdateForm(request.POST,instance=request.user.persona)
			messages.error(request,'Hay errores en algun campo')

			context = {
			'user_form':user_form,
			'persona_form':persona_form
			}
			return render(request, 'cuenta/editar.html', context)

