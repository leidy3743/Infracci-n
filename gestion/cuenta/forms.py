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

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from persona.models import Persona
from django.forms.widgets import ClearableFileInput
from inicio.mixins import LoginRequiredMixin


"""FormView: Es una vista que muestra un formulario. En caso de error, vuelve a mostrar 
	el formulario con errores de validación; en caso de éxito, redirige a una 
	nueva URL"""
class UserUpdateForm(LoginRequiredMixin, forms.ModelForm):
	"""Permite crear el formulario de la cuenta de usuario"""

	first_name = forms.CharField(label='Nombre')
	last_name = forms.CharField(label='Apellido')
	email = forms.CharField(label='Correo electronico')

	class Meta:
		"""Permite determinar del modelo Usuario, los campos first_name, last_name y email 
		   que se muestran en el formulario"""
		model = User
		fields = ('first_name','last_name','email')

"""PasswordChangeForm: Es una vista que permite cambiar la contraseña del usuario"""
class UserPasswordUpdateForm(LoginRequiredMixin, PasswordChangeForm):
	"""Permite crear un formulario para cambiar la contraseña del usuario"""
	new_password1 = forms.CharField(label='Nueva contraseña',widget=forms.PasswordInput)
	new_password2 = forms.CharField(label='Confirmacion nueva contraseña',widget=forms.PasswordInput)
	old_password = forms.CharField(label='Contraseña antigua',widget=forms.PasswordInput)

#FormView
class PersonaUpdateForm(LoginRequiredMixin, forms.ModelForm):
	"""Permite crear un formulario para los datos de persona"""
	class Meta:
		"""Permite determinar del modelo Persona, los campos identificacion, direccion, 
		   telefono e imagen que se muestran en el formulario"""
		model = Persona
		fields = ('identificacion','sede','cargo','tipo', 'imagen')