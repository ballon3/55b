# Register your models here.
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from events.models import Event

admin.site.register(Event)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
