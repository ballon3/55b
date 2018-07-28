from django.db import models

# Create your models here.
class Space(models.Model):
    #Here we define a space model, 
    # illustrating a location in which 
    # users will share common experiences 
    # and interactions
    name = models.TextField(null=True)
    venue_id = models.TextField()
    checkins = models.IntegerField(unique=True)
    latitude = models.TextField()
    longitude = models.TextField()
    address = models.TextField()
    email = models.EmailField()
    country = models.CharField(null=True, max_length=80)
    zipcode = models.CharField(null=True, max_length=15)
    industry = models.CharField(null=True, max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
	#updated_at = models.DateTimeField(auto_now_add=True)	

    def __str__(self):
        return self.name

