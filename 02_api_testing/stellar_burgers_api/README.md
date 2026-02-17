#  API тесты для Stellar Burgers

## Описание: 

**Цель:** Написать автотесты для API сервиса Stellar Burgers с использованием Allure-отчетов.
  
[**Тестовый стенд**](https://stellarburgers.education-services.ru)

[**Документация API**](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/Api-Stellar_Burgers.pdf)


## Технологии
- Pytest 
- Requests 
- Allure-pytest 

## Структура проекта

Этот проект является частью портфолио `QA_profile`. 

**Расположение в портфолио:** 
`QA_profile/02_api_testing/stellar_burgers_api/`

После клонирования всего репозитория перейдите в эту папку для работы с проектом.

**`src/`** - пакет с API клиентами и вспомогательными модулями
- `__init__.py`
- `base_api.py` - базовый класс для API запросов
- `user_api.py` - методы для работы с пользователями (регистрация, авторизация, выход)
- `order_api.py` - методы для работы с заказами (создание заказа)
- `data_generator.py` - генераторы тестовых данных
- `endpoints.py` - URL endpoints API (только используемые в проекте)
- `data.py` - константы, ожидаемые ответы и тестовые данные

**`tests/`** - пакет с тестами
- `__init__.py`
- `test_user_creation.py` - тесты создания пользователя
- `test_user_login.py` - тесты авторизации пользователя
- `test_order_creation.py` - тесты создания заказа

**Основные файлы в корне проекта:**
- `conftest.py` - фикстуры Pytest
- `requirements.txt` - зависимости проекта
- `README.md` - документация
- `.gitignore` - игнорируемые файлы
- `allure-results/` - результаты для генерации Allure отчетов

## Что тестируется

### 1. Создание пользователя (POST /api/auth/register)
- Создать уникального пользователя
- Создать пользователя, который уже зарегистрирован
- Создать пользователя без одного из обязательных полей

### 2. Логин пользователя (POST /api/auth/login)
- Вход под существующим пользователем
- Вход с неверным логином и паролем

### 3. Создание заказа (POST /api/orders)
- С авторизацией 
- Без авторизации 
- С ингредиентами 
- Без ингредиентов 
- С неверным хешем ингредиентов

##  Установка и запуск

### 1. Клонирование и настройка
```bash
# Клонирование портфолио и переход в папку проекта 
git clone https://github.com/Crypt0mnesia/QA_profile.git
cd QA_profile/02_api_testing/stellar_burgers_api/

# Создание виртуального окружения
python -m venv .venv

# Активация виртуального окружения
source .venv/bin/activate  # MacOS/Linux
.venv\Scripts\activate     # Windows
```
### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```
### 3. Запуск тестов

```bash
# Все тесты с Allure отчетом
pytest tests/ --alluredir=allure-results

# Конкретные тесты
pytest tests/test_user_creation.py -v
pytest tests/test_user_login.py -v
pytest tests/test_order_creation.py -v

```
### 4. Генерация и просмотр Allure отчета
```bash
# Генерация HTML отчета
allure generate allure-results -o allure-report --clean

# Просмотр отчета в браузере:
allure open allure-report
# или откройте файл allure-report/index.html в браузере
```
