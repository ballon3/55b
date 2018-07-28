from rest_framework import serializers
from spaces.models import Space

class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = ('name','latitude','longitude', 'zipcode', 'address','country', 'industry','email','venue_id', 'is_active',
			'checkins','created_at')

   