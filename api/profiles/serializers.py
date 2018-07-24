from profiles.models import MyUser
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('first', 'last', 'email', 'industry', 'headline', 'country', 'zipcode',)