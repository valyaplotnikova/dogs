from django.contrib import admin

from dogs.models import Breed, Dog


admin.site.register(Dog)
admin.site.register(Breed)
