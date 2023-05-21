from django.db import models
from django.core import validators

import datetime
import uuid

# Create your models here.
class Patient(models.Model):
	patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	first_name = models.CharField(max_length=50, default="FirstName")
	last_name = models.CharField(max_length=50, default="LastName")
	dob = models.DateField(default=datetime.date.today)

	def __str__(self):
		today = datetime.date.today()
		age = today.year - self.dob.year - ((today.month, today.day) < (dob.month, dob.day))
		return f'Name: {first_name} {last_name}; Age: {age}'

class MedicalRecord(models.Model):
	patient_id = models.ForeignKey(Patient, default=uuid.uuid4, on_delete=models.CASCADE)
	rec_type = models.CharField(max_length=100, default="Blood Pressure")
	rec_value = models.CharField(max_length=100, default="0/0 mm of Hg")
	day = models.IntegerField(
		default=1, 
		validators=[
			validators.MinValueValidator(1),
			validators.MaxValueValidator(31)
		]
	)
	month = models.IntegerField(
		default=1, 
		validators=[
			validators.MinValueValidator(1),
			validators.MaxValueValidator(12)
		]
	)
	year = models.IntegerField(
		default=2023, 
		validators=[validators.MinValueValidator(2023),]
	)

	def __str__(self):
		return f'{self.patient_id}: {self.day}-{self.month}-{self.year}'