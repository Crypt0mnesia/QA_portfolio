# UI-тесты для Stellar Burgers

## О проекте
Проект содержит UI-автотесты для веб-приложения Stellar Burgers. 
Выполнен в рамках дипломной работы курса «Инженер по тестированию» в Яндекс.Практикуме (часть 3).

**Цель:** Проверка ключевых пользовательских сценариев с использованием Page Object Model, кросс-браузерного тестирования и Allure-отчётов.

[**Тестовый стенд**](https://stellarburgers.education-services.ru)


## Технологии
*   Python, Pytest, Selenium WebDriver
*   Page Object Model
*   Allure-pytest
*   Page Object Pattern
*   Chrome / Firefox (кросс-браузерность)
*   Seletools (для Drag-and-Drop)


## Структура проекта (в составе портфолио)
Этот проект является частью портфолио `QA_profile`. 

**Расположение в портфолио:** 
`QA_profile/01_ui_testing/stellar_burgers_ui_crossbrowser/`

После клонирования всего репозитория перейдите в эту папку для работы с проектом.


**Основные файлы в корне:**
*   `conftest.py` - фикстуры Pytest с параметризацией для браузеров
*   `pytest.ini` - конфигурация для Allure-отчетов
*   `requirements.txt` - зависимости проекта
*   `README.md` - документация
*   `allure-results/` - результаты для генерации Allure отчетов


**Пакеты с Page Object и вспомогательными модулями:**




**pages/ - классы Page Object**


*   `__init__.py`
*   `base_page.py` - базовый класс с методами ожидания и перетаскивания
*   `main_page.py` - методы для работы с конструктором бургеров
*   `order_feed_page.py` - методы для работы с лентой заказов


**locators/ - локаторы элементов**


*   `__init__.py`
*   `main_page_locators.py` - локаторы главной страницы и конструктора
*   `auth_locators.py` - локаторы формы авторизации
*   `order_feed_locators.py` - локаторы ленты заказов


**helpers/ - вспомогательные модули**


*   `__init__.py`
*   `urls.py` - URL используемые в проекте
*   `data.py` - константы, учетные данные и настройки


**tests/ - пакет с тестами**
*   `__init__.py`
*   `test_constructor.py` - 5 тестов основной функциональности конструктора
*   `test_order_feed.py` - 3 теста для раздела ленты заказов


## Что тестируется
### Основная функциональность (5 проверок)
1.  Переход по клику на «Конструктор»
2.  Переход по клику на раздел «Лента заказов»
3.  Появление всплывающего окна с деталями при клике на ингредиент
4.  Закрытие всплывающего окна кликом по крестику
5.  Увеличение счетчика ингредиента при добавлении в заказ


### Раздел «Лента заказов» (3 проверки)
6.  Увеличение счетчика «Выполнено за всё время» при создании заказа
7.  Увеличение счетчика «Выполнено за сегодня» при создании заказа
8.  Появление номера заказа в разделе «В работе»

## Установка и запуск
1. клонирование и настройка
```bash
# Клонировать портфолио и перейти в папку проекта
git clone https://github.com/Crypt0mnesia/QA_profile.git
cd QA_profile/01_ui_testing/stellar_burgers_ui_crossbrowser


# Создать виртуальное окружение
python -m venv .venv

# Активировать виртуальное окружение
source .venv/bin/activate  # MacOS/Linux
.venv\Scripts\activate     # Windows
```

2. Установка зависимостей
```bash
pip install -r requirements.txt
```

3. Запуск тестов
```bash
# Все тесты (автоматически в Chrome и Firefox)
pytest tests/ -v

# Конкретные тесты
pytest tests/test_constructor.py -v
pytest tests/test_order_feed.py -v

# Запуск тестов с генерацией Allure-отчетов
pytest tests/ -v --alluredir=allure-results
```

4. Генерация и просмотр Allure-отчета
```bash
# Генерация HTML отчета
allure generate allure-results -o allure-report --clean

# Просмотр отчета в браузере:
allure open allure-report
# или откройте файл allure-report/index.html в браузере
```

