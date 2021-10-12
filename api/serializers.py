from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Person, PersonOnlineData

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'person_detail_api'}
        }

class PersonOnlineSerializer(serializers.ModelSerializer):
    #person = serializers.StringRelatedField()
    person = PersonSerializer()
    class Meta:
        model = PersonOnlineData
        fields = '__all__'