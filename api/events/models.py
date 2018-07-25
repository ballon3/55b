from django.db import models

# Create your models here.
class Event(models.Model):
   
    title = models.TextField(null=True)
    country = models.CharField(null=True, max_length=80)
    zipcode = models.CharField(null=True, max_length=15)
    industry = models.CharField(null=True, max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

