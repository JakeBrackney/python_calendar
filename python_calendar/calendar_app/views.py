from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import Event

def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, 'calendar_app/event_detail.html', {'event': event})

def index(request):
    return render(request, 'calendar_app/base.html')

def signup(request):
    form = UserCreationForm
    context = {'form' : form}
    return render(request, 'registration/signup.html', context)

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