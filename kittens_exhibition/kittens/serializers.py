from rest_framework import serializers
from .models import Kitten, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']

class KittenSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Kitten
        fields = ['id', 'name', 'color', 'age_in_months', 'description', 'breed', 'owner']
