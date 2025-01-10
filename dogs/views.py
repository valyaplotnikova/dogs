from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Avg, Count, Prefetch, OuterRef, Subquery
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer


class DogViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления собаками.

    Этот ViewSet предоставляет методы для получения списка собак и информации о конкретной собаке.
    """
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def list(self, request, *args, **kwargs):
        """
        Получает список всех собак с информацией о среднем возрасте каждой породы.

        Args:
            request: HTTP запрос.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            Response: Ответ с сериализованным списком собак и их средним возрастом.
        """
        breeds = Breed.objects.annotate(avg_age=Avg('dogs__age'))
        breed_avg_age_dict = {breed.id: breed.avg_age for breed in breeds}
        dogs = Dog.objects.select_related('breed')
        serializer = self.get_serializer(dogs, many=True)

        for dog_data in serializer.data:
            breed_id = dog_data['breed']
            dog_data['avg_age'] = breed_avg_age_dict.get(breed_id, None)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Создает новую собаку.

        Args:
            request: HTTP запрос с данными собаки.

        Returns:
            Response: Ответ с сериализованными данными созданной собаки.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
        Получает информацию о конкретной собаке, включая количество собак той же породы.

        Args:
            request: HTTP запрос.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            Response: Ответ с сериализованными данными о собаке и количеством собак той же породы.
            Если собака не найдена, возвращает 404 Not Found.
        """
        try:
            dog = self.get_object()  # Получаем объект собаки по первичному ключу
            breed_count = Dog.objects.filter(breed=dog.breed).count()  # Считаем количество собак той же породы
            serializer = self.get_serializer(dog)
            data = serializer.data
            data['breed_count'] = breed_count  # Добавляем количество собак той же породы в ответ
            return Response(data, status=status.HTTP_200_OK)  # Возвращаем успешный ответ
        except Dog.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        """
        Обновляет информацию о конкретной собаке.

        Args:
            request: HTTP запрос с обновленными данными собаки.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            Response: Ответ с сериализованными данными обновленной собаки.
            Если собака не найдена, возвращает 404 Not Found.
        """
        dog = self.get_object()
        serializer = self.get_serializer(dog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Удаляет конкретную собаку.

        Args:
            request: HTTP запрос.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            Response: Ответ с сообщением об успешном удалении.
            Если собака не найдена, возвращает 404 Not Found.
        """
        dog = self.get_object()
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления породами собак.

    Этот ViewSet предоставляет методы для получения списка пород и информации о конкретной породе.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def list(self, request, *args, **kwargs):
        """
        Получает список всех пород с количеством собак каждой породы.

        Args:
            request: HTTP запрос.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            Response: Ответ с сериализованным списком пород и количеством собак каждой породы.
        """
        dogs_count_subquery = Dog.objects.filter(breed=OuterRef('pk')).values('breed').annotate(
            count=Count('id')).values('count')
        breeds = self.queryset.annotate(dogs_count=Subquery(dogs_count_subquery))
        serializer = self.get_serializer(breeds, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Создает новую породу.

        Args:
            request: HTTP запрос с данными породы.

        Returns:
            Response: Ответ с сериализованными данными созданной породы.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
        Получает информацию о конкретной породе.

        Args:
            request: HTTP запрос.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            Response: Ответ с сериализованными данными о породе.
            Если порода не найдена, возвращает 404 Not Found.
        """
        try:
            breed = self.get_object()
            serializer = self.get_serializer(breed)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Breed.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        """
        Обновляет информацию о конкретной породе.

        Args:
            request: HTTP запрос с обновленными данными породы.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            Response: Ответ с сериализованными данными обновленной породы.
            Если собака не найдена, возвращает 404 Not Found.
        """
        breed = self.get_object()
        serializer = self.get_serializer(breed, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Удаляет конкретную породу.

        Args:
            request: HTTP запрос.
            *args: Дополнительные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            Response: Ответ с сообщением об успешном удалении.
            Если порода не найдена, возвращает 404 Not Found.
        """
        breed = self.get_object()
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
