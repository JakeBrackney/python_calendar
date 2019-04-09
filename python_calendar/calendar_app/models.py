from django.db import models

# Create your models here.

class Event(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField()
	startTime = models.TimeField()
	endTime = models.TimeField()
	description = models.TextField()
	location = models.CharField(max_length=400)

	def __str__(self):
		return self.title