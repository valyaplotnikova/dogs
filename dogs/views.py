from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Avg, Count
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления собаками.
    """
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def list(self, request, *args, **kwargs):
        """
        Получает список всех собак с информацией о среднем возрасте каждой породы.
        """
        dogs = self.queryset.annotate(avg_age=Avg('age'))
        serializer = self.get_serializer(dogs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Получает информацию о конкретной собаке, включая количество собак той же породы.
        """
        dog = self.get_object()
        breed_count = Dog.objects.filter(breed=dog.breed).count()
        serializer = self.get_serializer(dog)
        data = serializer.data
        data['breed_count'] = breed_count
        return Response(data)


class BreedViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления породами собак.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def list(self, request, *args, **kwargs):
        """
        Получает список всех пород с количеством собак каждой породы.
        """
        breeds = self.queryset.annotate(dog_count=Count('dogs'))
        serializer = self.get_serializer(breeds, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Получает информацию о конкретной породе.
        """
        breed = self.get_object()
        serializer = self.get_serializer(breed)
        return Response(serializer.data)
