from django.shortcuts import render
from spaces.models import Space
# Create your views here.
from django.views.generic import TemplateView, View, ListView
from rest_framework import viewsets
from spaces.serializers import SpaceSerializer
# Create your views here.

class SpaceViewSet(viewsets.ModelViewSet):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
