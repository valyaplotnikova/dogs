from django.db import models


class Breed(models.Model):

    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]

    name = models.CharField(
        max_length=100,
        verbose_name='Название породы'
    )
    size = models.CharField(
        max_length=20,
        choices=SIZE_CHOICES,
        verbose_name='Размер породы'
    )
    friendliness = models.PositiveSmallIntegerField(
        choices=[i for i in range(1, 6)],
        verbose_name='Дружелюбие породы'
    )
    trainability = models.PositiveSmallIntegerField(
        choices=[i for i in range(1, 6)],
        verbose_name='Обучаемость породы'
    )
    shedding_amount = models.PositiveSmallIntegerField(
        choices=[i for i in range(1, 6)],
        verbose_name='Количество линьки шерсти'
    )
    exercise_needs = models.PositiveSmallIntegerField(
        choices=[i for i in range(1, 6)],
        verbose_name='Необходимые упражнения'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'
        ordering = ('name',)


class Dog(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name='Имя собаки'
    )
    age = models.PositiveSmallIntegerField(
        verbose_name='Возраст собаки'
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        verbose_name='Порода собаки'
    )
    gender = models.CharField(
        max_length=20,
        verbose_name='Пол собаки'
    )
    color = models.CharField(
        max_length=50,
        verbose_name='Цвет собаки'
    )
    favorite_food = models.CharField(
        max_length=100,
        verbose_name='Любимая еда собаки'
    )
    favorite_toy = models.CharField(
        max_length=100,
        verbose_name='Любимая игрушка собаки'
    )

    def __str__(self):
        return f'Собака {self.name}, породы {self.breed}, возраст {self.age}, пол {self.gender}, цвет {self.color}'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
        ordering = ('name',)
