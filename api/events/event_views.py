from django.shortcuts import render
from events.models import Event
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView
from rest_framework import viewsets
from events.serializers import EventSerializer
# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

"""
class EventView(View):
    def get(self, request, event_id):

        try:
            event = Event.objects.get(id=user_id)
        except:
            event = None

        context = {
            "viewed_user": event
        }

        return render(request, "user_profile.html", context)
"""