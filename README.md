# Tasks_Manager

## Установка и запуск
1. Клонируйте репозиторий:
   git clone <URL_вашего_репозитория>
2. Перейдите в директорию проекта:
   cd Task_Manager
3. Установите зависимости:
   pip install -r requirements.txt
4. Запуститте сервер:
   python manage.py runserver

## Swagger для тестирования API:
  Перейдите по адресу  http://localhost:8000/api/swagger/ в вашем браузере, 
  чтобы протестировать API с помощью Swagger UI.
  POST /tasks/
  {
    "title": "Пример задачи"
  }
  
  GET /tasks/
  {
    "id": 1,
    "title": "Пример задачи",
    "is_complete": false
  }
