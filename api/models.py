from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    headline = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.email
