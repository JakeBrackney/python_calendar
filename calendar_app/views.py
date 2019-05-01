from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import calendar
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

# Create your views here.
from .models import Event
from .utils import Calendar
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from datetime import datetime, timedelta, date
from calendar import HTMLCalendar

# from https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html
class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar_app/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

# from https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html
def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def index(request):
    return render(request, 'calendar_app/base.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/signup.html', context)

@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'calendar_app/event_form.html', {'form': form})

@login_required 
def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, 'calendar_app/event_detail.html', {'event': event})

@login_required
def event_edit(request, pk):
    event = Event.objects.get(id=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', pk = event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'calendar_app/event_form.html', {'form' : form})

@login_required
def event_delete(request, pk):
    Event.objects.get(id=pk).delete()
    return redirect('event_form')

# def sign_up(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})