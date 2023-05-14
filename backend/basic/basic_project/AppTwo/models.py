from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=100, default="FirstName")
	last_name = models.CharField(max_length=100, default="LastName")
	email = models.EmailField(max_length=300, default="sample@sample.com", unique=True)

	def __str__(self):
		return f'{self.first_name} {self.last_name} [Contact at: {self.email}]'