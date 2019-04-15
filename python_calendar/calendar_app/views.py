from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm

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