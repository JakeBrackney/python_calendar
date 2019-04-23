from django.db import models
from datetime import datetime, date
from django.utils.timezone import now
# Create your models here.

class Event(models.Model):
	title = models.CharField(max_length=100)
	startDate = models.DateField(("Date"), default=date.today)
	startTime = models.TimeField(default=now)
	endDate = models.DateField(blank=True)
	endTime = models.TimeField(blank=True)
	# startTime = models.TimeField()
	# endTime = models.TimeField()
	description = models.TextField()
	location = models.CharField(max_length=400)

	def __str__(self):
		return self.title

	# def __init__(self, *args, **kwargs):
	# 	super(EventForm, self).__init__(*args, **kwargs)
  #   self.fields['trans_date'].initial