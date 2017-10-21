from .models import Greeting
from rest_framework import serializers


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Greeting
        fields = ('when', 'extra_field', 'my_field')
