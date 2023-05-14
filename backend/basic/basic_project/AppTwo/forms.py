from django import forms
from django.core import validators

from AppTwo.models import User

# form model here

class RegisterUserForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	verifyemail = forms.EmailField(label="Re-enter your email to confirm")

	def clean(self):
		all_clean_data = super().clean()

		email = all_clean_data['email']
		verify_email = all_clean_data['verifyemail']

		if email != verify_email:
			raise forms.ValidationError("Emails do not match")

class SignUpForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'
	

