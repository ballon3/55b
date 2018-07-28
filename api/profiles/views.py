from django.shortcuts import render
from profiles.models import MyUser
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView
from rest_framework import viewsets
from profiles.serializers import UserSerializer
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
import requests


class HomePageView(ListView):
    model = MyUser

class FriendViewsSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class UserProfileView(View):
    def get(self, request, user_id):

        try:
            user = MyUser.objects.get(id=user_id)
        except:
            user = None

        context = {
            "viewed_user": user
        
        }

        return render(request, "user_profile.html", context)
