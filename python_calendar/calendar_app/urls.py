from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('signup', views.signup, name='signup'),
    path('event_form', views.event_create, name='event_form'),
    path('event/<int:pk>', views.event_detail, name='event_detail'),
    path('event/<int:pk>/event_edit', views.event_edit, name='event_edit'),
]


# urlpatterns = [
#      # Login / Log Out
#      path('accounts/login/', auth_views.LoginView,
#           {'template_name': 'accounts/login.html'}, name='login'),
#      path('accounts/logout/', auth_views.LogoutView,
#           {'template_name': 'accounts/logged_out.html'}, name='logout'),
#           # Sign Up
#      path('accounts/signup', views.sign_up, name="signup")
# ]