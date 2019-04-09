from django.shortcuts import render

# Create your views here.
from .models import Event

def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, 'calendar_app/event_detail.html', {'event': event})