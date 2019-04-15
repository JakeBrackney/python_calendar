from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
     # Login / Log Out
     path('accounts/login/', auth_views.LoginView,
          {'template_name': 'accounts/login.html'}, name='login'),
     path('accounts/logout/', auth_views.LogoutView,
          {'template_name': 'accounts/logged_out.html'}, name='logout'),
          # Sign Up
     path('accounts/signup', views.sign_up, name="signup")
]
