from django import forms
from django.core import validators

from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']