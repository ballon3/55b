# pages/urls.py
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from . import event_views

urlpatterns = [
    url(r'event/(?P<event_id>\w+)$', event_views.EventView.as_view(), name='event_profile',),
    
    #path('', views.HomePageView.as_view(), name='home'),

]