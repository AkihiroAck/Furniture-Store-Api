# Furniture-Store-Api

## Оглавление
1. [Описание проекта](#описание-проекта)
2. [Быстрый запуск](#быстрый-запуск)
   1. [Клонирование репозитория](#1-клонирование-репозитория)
   2. [Настройка переменных окружения](#2-настройка-переменных-окружения)
   3. [Запуск с помощью Docker Compose](#3-запуск-с-помощью-docker-compose)
   4. [Создание superuser](#4-создание-superuser)
6. [Используемые порты](#используемые-порты)
7. [Структура API](#структура-api)
8. [Технологии](#технологии)

---

## Описание проекта

**Furniture-Store-Api** - Это REST API для магазина мебели, реализованный на Django + Django REST Framework.

---

## Быстрый запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/AkihiroAck/Furniture-Store-Api.git
cd Furniture-Store-Api
````

### 2. Настройка переменных окружения
Создайте файл `.env` в корневой папке (рядом с `docker-compose.yml`) и настройте его под ваши нужды:

Пример содержимого:
```env
# Django
SECRET_KEY=django-insecure-*&npc-eipi)b&z!#7e-dppx#0h^ex2)^3)qgyxtxtjf#&(y=xq
DEBUG = True
EMAIL_BACKEND_TEST = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'noreply@xxlmebel.com'
EMAIL_HOST_PASSWORD = 'email_password'

# PostgreSQL
POSTGRES_DATABASE_NAME=POSTGRESQL_DATABASE_NAME
POSTGRES_USERNAME=db_user
POSTGRES_PASSWORD=db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# pgAdmin
PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=1234
```

### 3. Запуск с помощью Docker Compose

```bash
docker-compose up --build
```

После запуска:

* API будет доступен на: **[localhost:8000/](http://localhost:8000/)**
* Админ-панель pgadmin4: **[localhost/80](http://localhost/80)**

### 4. Создание superuser

При необходимости можно создать superuser:

```bash
docker-compose exec backend python project/manage.py createsuperuser
```

---

##  Используемые порты

| Сервис      | В контейнере | На хосте | Назначение             |
| ----------- | ------------ | -------- | ---------------------- |
| Backend     | `8000`       | `8000`   | Django Rest Framework  |
| PostgreSQL  | `5432`       | `5432`   | СУБД PostgreSQL        |
| pgadmin4    | `5050`       | `80`     | Веб-интерфейс к БД     |

---

## Структура API

### Мебели

#### `GET /furniture/`
Возвращает список всей доступной мебели.
Можно фильтровать данные по категории `?category=category_name`

#### `GET /furniture/:id/`
Возвращает детальную информацию о конкретном товаре по его id.

### Заказы

#### `POST /orders/`
Создаёт новый заказ.
Тело запроса (JSON):
```json
{
  "customer_email": "test@example.com",
  "furnitures": [1, 2, 3]
}
```
Действия:
- Сохраняет заказ
- Рассчитывает итоговую сумму (`total_price`)
- Возвращает созданный объект заказа


#### `GET /orders/`
Возвращает список заказов по email клиента.
Можно фильтровать данные по почте `?email=client_email`

---

## Технологии

* Python 3.12.10
* Django 5.2.6
* Django REST Framework 3.16.1
* PostgreSQL 17.4
* Docker / Docker Compose