from django.db import models
from datetime import datetime
# Create your models here.

class Event(models.Model):
	title = models.CharField(max_length=100)
	startDate = models.DateTimeField(default=datetime.now)
	endDate = models.DateTimeField(blank=True)
	# startTime = models.TimeField()
	# endTime = models.TimeField()
	description = models.TextField()
	location = models.CharField(max_length=400)

	def __str__(self):
		return self.title