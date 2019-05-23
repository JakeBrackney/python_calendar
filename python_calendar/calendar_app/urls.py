from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('signup', views.signup, name='signup'),
    path('event_form', views.event_create, name='event_form'),
    path('event/<int:pk>', views.event_detail, name='event_detail'),
    path('event/<int:pk>/event_edit', views.event_edit, name='event_edit'),
    path('event/<int:pk>/event_delete', views.event_delete, name='event_delete'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^calendar/event/<int:pk>', views.event_detail, name='event_detail'), # here
]