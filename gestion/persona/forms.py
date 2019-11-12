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
from django import forms
from models import *
from django.forms.extras.widgets import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse
from inicio.mixins import LoginRequiredMixin
from .models import Persona
from django.contrib.auth.models import User
from django.core import validators
from django.core.validators import EmailValidator

#FormView
class UserForm(LoginRequiredMixin, UserCreationForm):
	"""Permite crear un formulario con los campos del usuario"""

	username = forms.CharField(label='Nombre de Usuario')
	email = forms.EmailField(label='Correo Electrónico')
	first_name = forms.CharField(label='Nombres' )
	last_name = forms.CharField(label='Apellidos')
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)


	def clean_first_name(self):
		"""Permite validar que el campo nombre sólo contenga letras[A-Z],[a-z]"""

		n=0
		nombre = self.cleaned_data['first_name']
		if nombre.isalpha():
			return nombre
		else:
			if " " in nombre:
				separar=nombre.split(" ")
				for c in range(len(separar)):
					if separar[c].isalpha():
						n=n+1
					else:
						n=-1
						break
				if n>0:
					return nombre
				else:
					if n<0:
						raise forms.ValidationError("El Nombre solo puede contener letras.")
			else:
				raise forms.ValidationError('El Nombre solo puede contener letras.')


	def clean_last_name(self):
		"""Permite validar que el campo apellido sólo contenga letras[A-Z],[a-z]"""

		n=0
		apellido = self.cleaned_data['last_name']
		if apellido.isalpha():
			return apellido
		else:
			if " " in apellido:
				separar=apellido.split(" ")
				for c in range(len(separar)):
					if separar[c].isalpha():
						n=n+1
					else:
						n=-1
						break
				if n>0:
					return apellido
				else:
					if n<0:
						raise forms.ValidationError('El Apellido solo puede contener letras.')
			else:
				raise forms.ValidationError('El Apellido solo puede contener letras.')

	class Meta:
		"""Permite determinar el modelo User y los campos username, email, first_name,
			last_name que se muestran en el formulario Usuario"""
		model = User
		fields = ( "username", "email", "first_name", "last_name")	

#FormView
class PersonaForm(LoginRequiredMixin, forms.ModelForm):
	"""Permite mostrar un formulario con la información de Persona"""

	identificacion = forms.CharField(label='Número de Identificación')
	cargo = forms.CharField(label='Cargo Laboral')
	tipo = forms.CharField(widget=forms.Select(choices=tipo_usuario), label='Tipo de Usuario')

	def clean_identificacion(self):
		"""Permite validar que el campo identificacion sólo contenga números[0-9] y 
		su longitud sea de 10 digitos"""

		identificacion = self.cleaned_data['identificacion']
		if not identificacion.isdigit():
			raise forms.ValidationError('El Número de Identificación solo puede contener números.')
		elif len(identificacion) > 12:
			raise forms.ValidationError('La longitud del Número de Identificación debe ser menor o igual a 12 dígitos.')
		else:
			return identificacion
			

	def clean_cargo(self):
		"""Permite validar que el campo cargo_laboral sólo contenga letras[A-Z],[a-z]"""

		n=0
		cargolaboral = self.cleaned_data['cargo']
		if cargolaboral.isalpha():
			return cargolaboral
		else:
			if " " in cargolaboral:
				separar=cargolaboral.split(" ")
				for c in range(len(separar)):
					if separar[c].isalpha():
						n=n+1
					else:
						n=-1
						break
				if n>0:
					return cargolaboral
				else:
					if n<0:
						raise forms.ValidationError('El Cargo Laboral solo puede contener letras.')
			else:
				raise forms.ValidationError('El Cargo Laboral solo puede contener letras.')

	class Meta:
		"""Permite determinar el modelo Persona y los campos identificacion, telefono, 
		direccion, empresa, cargolaboral, imagen, tipo, descripciontu, estado y peajes 
		que se muestran en el formulario"""

		model = Persona
		fields = ['identificacion', 'sede', 'cargo', 'imagen', 'tipo',]

"""CreateView: Es una vista que muestra un formulario para crear un objeto. Si hay 
errores muestra mensajes de error y si no, guarda el objeto"""	
class PersonaCreateView(LoginRequiredMixin, TemplateView):
	"""Permite mostrar el formulario para crear un usuario"""


	def get(self,request,*args,**kwargs):
		"""Permite desplegar el formulario de creación de usuario y personal para un 
		peaje"""

		user_form = UserForm()
		persona_form = PersonaForm()
		forms = [user_form, persona_form]
		context = {
		'section_title':'Crear Empleado',
		'user_form':user_form,
		'persona_form':persona_form }

		return render(request, 'persona/persona_form.html', context)


	def post(self,request,*args,**kwargs):
		"""Permite enviar el formulario con la información de la persona, si es valido 
		guarda los datos de lo contrario redirecciona al usuario a la lista de personas"""

		user_form = UserForm(request.POST)
		persona_form = PersonaForm(request.POST,request.FILES)

		if user_form.is_valid() and persona_form.is_valid():
			new_user = user_form.save()
			new_persona = persona_form.save(commit=False)
			new_persona.user = new_user
			new_persona.save()
			messages.info(request,'Nuevo usuario creado con exito')
			url = reverse('persona:listar-personas')

			return HttpResponseRedirect(url)

		user_form = UserForm(request.POST)
		persona_form = PersonaForm(request.POST)
		messages.error(request,'Hay errores en algun campo, revise el formulario')

		context = {
		'section_title':'Crear Empleado',
		'user_form':user_form,
		'persona_form':persona_form }

		return render(request, 'persona/persona_form.html', context)


"""UpdateView: Una vista que muestra un formulario para editar un objeto existente, en 
caso de un error retornar el formulario, de lo contrario guarda los cambios. Esto utiliza 
un formulario generado automáticamente a partir de la clase del modelo del objeto """
class PersonaUpdateView(LoginRequiredMixin, TemplateView):
	""" Permite actualizar la información de una persona """


	def get(self, request, *args, **kwargs):
		"""Permite obtener el id y los datos almacenados en la base de datos del usuario
			que se quiere editar"""

		persona = Persona.objects.get(id=kwargs['epk'])
		user = persona.user
		persona_form = PersonaForm(instance=persona)
		user_form = UserForm(instance=user)

		context = {
		'section_title':'Actualizar Empleado',
		'user_form':user_form,
		'persona_form':persona_form }

		return render(request, 'persona/persona_form.html', context)


	def post(sel, request, *args, **kwargs):
		"""Permite enviar la información modificada del personal a la base de datos, 
		si es valido guarda los datos de lo contrario muestra un mensaje de error y 
		vuelve a cargar el formulario para modificar Personal"""
		
		persona = Persona.objects.get(id=kwargs['epk'])
		user = persona.user

		persona_form = PersonaForm(request.POST,request.FILES,instance=persona)
		user_form = UserForm(request.POST,request.FILES,instance=user)

		if user_form.is_valid() and persona_form.is_valid():

			persona.identificacion = persona_form.cleaned_data['identificacion']
			persona.sede = persona_form.cleaned_data['sede']
			persona.cargo = persona_form.cleaned_data['cargo']
			persona.imagen = persona_form.cleaned_data['imagen']
			persona.tipo = persona_form.cleaned_data['tipo']
			persona.save()

			user.username = user_form.cleaned_data['username']
			user.first_name = user_form.cleaned_data['first_name']
			user.last_name = user_form.cleaned_data['last_name']
			user.email = user_form.cleaned_data['email']

			password1 = user_form.cleaned_data['password1']
			password2 = user_form.cleaned_data['password2']


			if password1 != "" and password2 != "":
				user.set_password(user_form.cleaned_data['password1'])
			user.save()

			""" En caso de que el administrador este modificando su misma cuenta de 
			usuario, es necesario que vuelva a ser logeado con los nuevos datos username
			y password """
			if user.id == request.user.id:
				user = authenticate(username=user.username,password=password1)
				if user is not None:
					if user.is_active:
						login(request,user)

			messages.info(request,'Usuario modificado con exito')
			url = reverse('persona:listar-personas')

			return HttpResponseRedirect(url)
		else:
			persona_form = PersonaForm(request.POST,request.FILES)
			user_form = UserForm(instance=user)

			context = {
			'section_title':'Actualizar Empleado',
			'user_form':user_form,
			'persona_form':persona_form }

			return render(request, 'persona/persona_form.html',context)


""" DeleteView: Una vista que muestra una página de confirmación y elimina un objeto existente """

class PersonaDeleteView(LoginRequiredMixin, DeleteView):
	"""Permite mientras se ejecuta contener el objeto persona sobre el que se esta 
	operando la vista"""
	
	model = Persona
	template_name = 'persona/persona_confirm_delete.html'
	success_url = reverse_lazy('persona:listar-personas')