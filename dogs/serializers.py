from rest_framework import serializers
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели породы.
    """
    class Meta:
        model = Breed
        fields = '__all__'


class DogSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели собаки.
    """
    class Meta:
        model = Dog
        fields = '__all__'
