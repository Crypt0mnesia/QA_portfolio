# Stellar Burgers — базовые UI-автотесты

## О проекте
UI-автотесты для веб-приложения  **[Stellar Burgers](https://stellarburgers.education-services.ru)** — космического фастфуда, где можно собрать и заказать бургер из необычных ингредиентов.
Проект выполнен в рамках обучения в Яндекс.Практикуме и демонстрирует навыки написания автоматизированных тестов для проверки ключевых пользовательских сценариев. 

**Тестовый стенд:** [https://stellarburgers.education-services.ru](https://stellarburgers.education-services.ru)


## Функциональность, покрытая тестами

### Регистрация
- Успешная регистрация с валидными данными
- Ошибка при регистрации с некорректным паролем

### Вход в систему
- Вход по кнопке «Войти в аккаунт» на главной
- Вход через кнопку «Личный кабинет»
- Вход через кнопку в форме регистрации
- Вход через кнопку в форме восстановления пароля

### Переход в личный кабинет
- Проверка перехода по клику на «Личный кабинет»

### Переход из личного кабинета в конструктор
- Проверка перехода по клику на «Конструктор»
- Проверка перехода по клику на логотип Stellar Burgers

### Выход из аккаунта
- Проверка выхода по кнопке «Выйти» в личном кабинете

### Раздел «Конструктор»
- Проверка переходов к разделам:
  - «Булки»
  - «Соусы»
  - «Начинки»

## Технологии

- Python 3.13
- Selenium WebDriver - для автоматизации браузера
- Pytest - фреймворк для тестирования
- Faker - генерация тестовых данных

## Структура проекта (в составе портфолио)
Этот проект является частью портфолио `QA_profile`. 

**Расположение в портфолио:** 
`QA_profile/01_ui_testing/stellar_burgers_ui/`

После клонирования всего репозитория перейдите в эту папку для работы с проектом.

### Тестовые сценарии
- **`tests/test_registration.py`** - Регистрация нового пользователя
- **`tests/test_login.py`** - Авторизация в системе 
- **`tests/test_personal_account.py`** - Работа с личным кабинетом
- **`tests/test_constructor_transition.py`** - Навигация по приложению
- **`tests/test_logout.py`** - - Выход из личного кабинета
- **`tests/test_constructor_sections.py`** - Конструктор бургеров

### Вспомогательные файлы
- **`locators.py`** - Селекторы элементов UI
- **`data.py`** - Константы, текстовые сообщения
- **`urls.py`** - URL страниц приложения
- **`generator.py`** - Утилиты для генерации данных
- **`helpers.py`** - Вспомогательные функции для тестов

### Конфигурация
- **`conftest.py`** - Фикстуры Pytest
- **`requirements.txt`** - Зависимости Python

## Установка и настройка

1. Клонируйте портфолио и перейдите в папку проекта
```bash
git clone https://github.com/Crypt0mnesia/QA_profile.git
cd QA_profile/01_ui_testing/stellar_burgers_ui
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```
3. Установите зависимости:
```bash 
pip install -r requirements.txt
```
4. Установите браузеры и драйверы:
- Установите Google Chrome (версия совместимая с Selenium)
- ChromeDriver (ручной установки  скачайте ChromeDriverс официального сайта; убедитесь, что версия ChromeDriver соответствует версии браузера; добавьте ChromeDriver в PATH системы)

## Запуск тестов
- Запуск всех тестов:
```bash
python -m pytest
```
- Запуск с подробным выводом:
```bash
python -m pytest -v
```
- Запуск конкретных тестовых файлов:
```bash
python -m pytest tests/test_registration.py -v
python -m pytest tests/test_login.py -v
python -m pytest tests/test_personal_account.py -v
python -m pytest tests/test_constructor_transition.py -v
python -m pytest tests/test_logout.py -v
python -m pytest tests/test_constructor_sections.py -v
```
