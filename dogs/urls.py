from django.urls import path, include
from rest_framework import routers

from dogs.apps import DogsConfig
from dogs.views import DogViewSet, BreedViewSet

app_name = DogsConfig.name

router = routers.DefaultRouter()
router.register(r'dogs', DogViewSet, basename='dogs')
router.register(r'breeds', BreedViewSet, basename='breeds')

urlpatterns = [
    path('', include(router.urls)),
]
