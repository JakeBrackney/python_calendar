from django import forms
from .models import Event
from datetime import datetime, date
from django.forms import ModelForm, DateInput
import datetime

class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'start_time', 'end_time', 'description', 'location')

    start_time = forms.DateTimeField(initial=(datetime.datetime.now().time),
    widget=forms.DateTimeInput(attrs={'type':'datetime-local', 'value':'datetime.now().time'}, format='%m/%d/%Y %I:%M %p')
    )

    end_time = forms.DateTimeField(initial=(datetime.datetime.now().time),
    widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%m/%d/%Y %I:%M %p')
    )

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)