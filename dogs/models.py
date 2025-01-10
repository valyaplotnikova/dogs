from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Breed(models.Model):
    """
    Модель для представления породы собаки.

    Attributes:
        name (str): Название породы.
        size (str): Размер породы (Tiny, Small, Medium, Large).
        friendliness (int): Дружелюбие (1-5).
        trainability (int): Обучаемость (1-5).
        shedding_amount (int): Количество линьки (1-5).
        exercise_needs (int): Потребности в физических упражнениях (1-5).
    """

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
        choices=[(i, i) for i in range(1, 6)],
        verbose_name='Дружелюбие породы'
    )
    trainability = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)],
        verbose_name='Обучаемость породы'
    )
    shedding_amount = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)],
        verbose_name='Количество линьки шерсти'
    )
    exercise_needs = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)],
        verbose_name='Необходимые упражнения'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'
        ordering = ('name',)


class Dog(models.Model):
    """
    Модель для представления собаки.

    Attributes:
        name (str): Имя собаки.
        age (int): Возраст собаки.
        breed (ForeignKey): Порода собаки.
        gender (str): Пол собаки.
        color (str): Цвет собаки.
        favorite_food (str): Любимая еда собаки.
        favorite_toy (str): Любимая игрушка собаки.
    """

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name = models.CharField(
        max_length=50,
        verbose_name='Имя собаки'
    )
    age = models.PositiveSmallIntegerField(
        verbose_name='Возраст собаки'
    )
    breed = models.ForeignKey(
        Breed,
        related_name='dogs',
        on_delete=models.SET_NULL,
        verbose_name='Порода собаки',
        **NULLABLE
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
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
