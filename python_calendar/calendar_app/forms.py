from django import forms
from .models import Event
from datetime import datetime, date

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'start_time', 'end_time', 'description', 'location')

    # startDate = forms.DateField(initial=date.today,
    # widget=forms.DateInput(format='%m/%d/%Y'),
    # )

    start_time = forms.DateTimeField(initial=(datetime.now().time),
    widget=forms.DateTimeInput(format='%m/%d/%Y %I:%M %p'),
        input_formats=('%m/%d/%Y %I:%M %p', )
    )

    # endDate = forms.DateField(
    # widget=forms.DateInput(format='%m/%d/%Y'),
    # input_formats=('%m/%d/%Y', )
    # )

    end_time = forms.DateTimeField(
    widget=forms.DateTimeInput(format='%m/%d/%Y %I:%M %p'),
    input_formats=('%m/%d/%Y %I:%M %p', )
    )