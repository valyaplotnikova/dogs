from rest_framework import serializers
from .models import Dog, Breed


class DogSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели собаки.
    """
    class Meta:
        model = Dog
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели породы.
    """
    dogs_count = serializers.IntegerField(read_only=True)

    def get_dogs_count(self, obj):
        return obj.dogs.count()

    class Meta:
        model = Breed
        fields = ('name', 'size', 'friendliness', 'trainability', 'shedding_amount', 'exercise_needs', 'dogs_count')
