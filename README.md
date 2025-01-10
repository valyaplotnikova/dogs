# Dog and Breed API

## Описание

Этот проект представляет собой RESTful API для управления данными о собаках и их породах. API позволяет пользователям создавать, получать, обновлять и удалять записи о собаках и породах, а также получать связанную информацию, такую как средний возраст собак по породам и количество собак для каждой породы.

## Структура проекта
  
Dogs/   
├──config/   
│ ├── init.py  
│ ├── settings.py   
│ ├── urls.py   
│ ├── wsgi.py   
│ └── asgi.py   
├──dogs/   
│ ├── migrations/   
│ ├── init.py   
│ ├── admin.py   
│ ├── apps.py  
│ ├── models.py   
│ ├── tests.py  
│ ├── views.py   
│ ├── urls.py   
├──fixtures/  
├──static/  
├── .env.example   
├── .flake8   
├── .gitignore   
├── docker-compose.yml  
├── Dockerfile  
├── manage.py  
├──  README.md   
└── requirements.txt  

## Основные компоненты проекта  
Проект API управления собаками и породами состоит из нескольких ключевых компонентов, которые обеспечивают его функциональность. Вот основные из них:

API: Основная часть проекта, реализующая RESTful API для взаимодействия с данными о собаках и породах. API обеспечивает создание, получение, обновление и удаление записей (CRUD) через различные эндпоинты.

*Модели:*

Dog: Модель, представляющая собаку. Содержит атрибуты, такие как имя, возраст, порода, пол, цвет и любимая еда.

Breed: Модель, представляющая породу собак. Содержит атрибуты, такие как название, размер, дружелюбие, обучаемость и потребности в физической активности.
## Эндпоинты API

### Модель Dog

- **Создание новой собаки**
  - **POST** `/api/dogs/`
  - **Тело запроса**:
    ```json
    {
      "name": "Buddy",
      "age": 3,
      "breed": 1,
      "gender": "Male",
      "color": "Brown",
      "favorite_food": "Chicken",
      "favorite_toy": "Ball"
    }
    ```
  - **Ответ**:
    ```json
    {
      "id": 1,
      "name": "Buddy",
      "age": 3,
      "breed": 1,
      "gender": "Male",
      "color": "Brown",
      "favorite_food": "Chicken",
      "favorite_toy": "Ball"
    }
    ```

- **Получение списка всех собак**
  - **GET** `/api/dogs/`
  - **Ответ**:
    ```json
    [
      {
        "id": 1,
        "name": "Buddy",
        "age": 3,
        "breed": {
          "id": 1,
          "name": "Labrador"
        },
        "average_age": 5
      },
      ...
    ]
    ```

- **Получение информации о конкретной собаке**
  - **GET** `/api/dogs/<id>`
  - **Ответ**:
    ```json
    {
      "id": 1,
      "name": "Buddy",
      "age": 3,
      "breed": 1,
      "gender": "Male",
      "color": "Brown",
      "favorite_food": "Chicken",
      "favorite_toy": "Ball",
      "breed_count": 10
    }
    ```

- **Обновление информации о собаке**
  - **PUT** `/api/dogs/<id>`
  - **Тело запроса**:
    ```json
    {
      "name": "Buddy",
      "age": 4,
      "breed": 1,
      "gender": "Male",
      "color": "Black",
      "favorite_food": "Beef",
      "favorite_toy": "Frisbee"
    }
    ```

- **Удаление записи о собаке**
  - **DELETE** `/api/dogs/<id>`
  - **Ответ**:
    ```json
    {
      "message": "Dog deleted successfully."
    }
    ```

### Модель Breed

- **Создание новой породы**
  - **POST** `/api/breeds/`
  - **Тело запроса**:
    ```json
    {
      "name": "Labrador",
      "size": "Large",
      "friendliness": 5,
      "trainability": 4,
      "shedding_amount": 2,
      "exercise_needs": 3
    }
    ```

- **Получение списка всех пород**
  - **GET** `/api/breeds/`
  - **Ответ**:
    ```json
    [
      {
        "id": 1,
        "name": "Labrador",
        "size": "Large",
        "dog_count": 10
      },
      ...
    ]
    ```

- **Получение информации о конкретной породе**
  - **GET** `/api/breeds/<id>`
  - **Ответ**:
    ```json
    {
      "id": 1,
      "name": "Labrador",
      "size": "Large",
      "friendliness": 5,
      "trainability": 4,
      "shedding_amount": 2,
      "exercise_needs": 3,
      "dog_count": 10
    }
    ```

- **Обновление информации о породе**
  - **PUT** `/api/breeds/<id>`
  - **Тело запроса**:
    ```json
    {
      "name": "Labrador Retriever",
      "size": "Large",
      "friendliness": 5,
      "trainability": 5,
      "shedding_amount": 2,
      "exercise_needs": 4
    }
    ```

- **Удаление записи о породе**
  - **DELETE** `/api/breeds/<id>`
  - **Ответ**:
    ```json
    {
      "message": "Breed deleted successfully."
    }
    ```

### Предварительные требования

- Убедитесь, что у вас установлен [Docker](https://www.docker.com/get-started) и [Docker Compose](https://docs.docker.com/compose/install/).

### Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/valyaplotnikova/dogs
   cd dogs
   ```
2. Создайте файл .env на основе файла .env.example и настройте переменные окружения.

3. Соберите и запустите контейнеры:
 ```bash
docker-compose up --build
```
После успешного запуска API будет доступно по адресу http://127.0.0.1:8000.

Для остановки контейнеров нажмите Ctrl + C или выполните:
 ```bash
docker-compose down
```