from django.db import models
import datetime

# Create your models here.
class Topic(models.Model):
	topic_name = models.CharField(max_length=300, unique=True, default="Topic Name")

	def __str__(self):
		return self.topic_name


class Webpage(models.Model):
	topic = models.ForeignKey(Topic, default="Topic Name", on_delete=models.CASCADE)
	name = models.CharField(max_length=50, unique=True, default="Webpage Name")
	url = models.URLField(unique=True, default="https://www.webpage.com")
	
	def __str__(self):
		return self.name


class AccessRecord(models.Model):
	name = models.ForeignKey(Webpage, default="Webpage name", on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)

	def __str__(self):
		return str(self.date)