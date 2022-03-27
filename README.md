# Тестовое задание. Рассылка. Фабрика Решений

## Проект реализован с помощью
Django 4.0.3, DRF, Celery, Flower

Запуск проекта

`git clone https://github.com/ds4tens/Fabrique <path>`

* Установить все необходимые зависимости

`pip install -r <path_to_project>/fabrique/requirements.txt`

* Передать в среду параметры
1. SECRET_KEY
2. DEBUG
3. DJANGO_HOSTS
4. SENDER_URL (url сервера реализацией рассылки в формате SENDER_URL /msg_id)
5. TOKEN (доступ к SENDER_URL)

Пример 
* SECRET_KEY="django-lotsofletters"
* DEBUG=0
* DJANGO_HOSTS="localhost,127.0.0.1,0.0.0.1"
* SENDER_URL="https://cool.server/v1337/send/"
* TOKEN="MEGATOKEN"

Провести миграции и можно запускать

# Для запуска контейнера dcoker так же нужны параметры

`docker-compose -up d`

# Документация OpenAPI

Документация доступна по `127.0.0.1:8000/swagger/` или `127.0.0.1:8000/redoc/`

Дашборд для модуля celery реализован через flower
доступ по `127.0.0.1:5555`
