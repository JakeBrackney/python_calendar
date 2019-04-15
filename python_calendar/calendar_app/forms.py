from django import forms
from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'startDate', 'startTime', 'endDate', 'endTime', 'description', 'location')

    startDate = forms.DateField(
    widget=forms.DateInput(format='%m/%d/%Y'),
    input_formats=('%m/%d/%Y', )
    )

    startTime = forms.TimeField(
    widget=forms.TimeInput(format='%I:%M %p'),
    input_formats=('%I:%M %p', )
    )

    endDate = forms.DateField(
    widget=forms.DateInput(format='%m/%d/%Y'),
    input_formats=('%m/%d/%Y', )
    )

    endTime = forms.TimeField(
    widget=forms.TimeInput(format='%I:%M %p'),
    input_formats=('%I:%M %p', )
    )