# Юнит-тесты для Stellar Burgers

## Описание
Юнит-тесты для классов приложения Stellar Burgers. Дипломный проект (часть 1).

**Цель:** Написать юнит-тесты для класса `Burger` с использованием моков и параметризации. Достичь 100% покрытия кода.

## Технологии
- Pytest 
- pytest-cov 


## Структура проекта
Этот проект является частью портфолио `QA_profile`. 

**Расположение в портфолио:** 
`QA_profile/03_unit_testing/stellar_burgers_unit/`

После клонирования всего репозитория перейдите в эту папку для работы с проектом.



**`praktikum/`** - пакет с исходным кодом программы
- `__init__.py`
- `bun.py` - класс Bun (булочка)
- `burger.py` - класс Burger (основной тестируемый класс)
- `database.py` - класс Database (база данных)
- `ingredient.py` - класс Ingredient (ингредиент)
- `ingredient_types.py` - константы типов ингредиентов

**`tests/`** - пакет с тестами
- `__init__.py`
- `test_burger.py` -  юнит-тесты для класса Burger

*Основные файлы в корне:*
- `conftest.py` - фикстуры Pytest с мок-объектами
- `requirements.txt` - зависимости проекта (pytest + pytest-cov)
- `praktikum.py` - главная программа
- `README.md` - документация
- `.gitignore` - игнорируемые файлы
- 
*Сгенерированные для проверки:*
- `htmlcov/` - папка с HTML отчетом о покрытии кода (включена для ревью) 

## Что протестировано
Протестированы все 7 методов класса `Burger`:
1. **`__init__()`** - инициализация бургера
2. **`set_buns()`** - установка булочки
3. **`add_ingredient()`** - добавление ингредиента
4. **`remove_ingredient()`** - удаление ингредиента по индексу
5. **`move_ingredient()`** - перемещение ингредиента
6. **`get_price()`** - расчет общей стоимости
7. **`get_receipt()`** - генерация чека с информацией о бургере

## Ключевые особенности тестов
- **100% покрытие** класса `burger.py` 
- **Использование моков** для изоляции класса Burger от зависимостей
- **Параметризация тестов** через `@pytest.mark.parametrize` для разных сценариев
- **Тестирование исключений** (`AttributeError`, `IndexError`)
- **Фикстуры Pytest** для переиспользования тестовых данных

## Установка и запуск

### 1. Клонирование портфолио, переход в папку проекта и настройка
```bash
git clone https://github.com/Crypt0mnesia/QA_profile.git
cd QA_profile/03_unit_testing/stellar_burgers_unit/
python -m venv .venv
source .venv/bin/activate  # MacOS/Linux
.venv\Scripts\activate     # Windows
```
### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```
### 3. Запуск тестов
```bash
## Все тесты
pytest tests/

# С подробным выводом
pytest tests/ -v

# С измерением покрытия
pytest tests/ --cov=praktikum.burger --cov-report=term

# Проверка 100% покрытия
pytest tests/ --cov=praktikum.burger --cov-report=term --cov-fail-under=100

# Генерация HTML отчета
pytest tests/ --cov=praktikum.burger --cov-report=html
```
### 4. Просмотр отчета о покрытии

**Для ревьюера:** 
Отчет уже сгенерирован и находится в папке `htmlcov/`. 
Откройте файл `htmlcov/index.html` в браузере для просмотра.


**Примечание:** Папка `htmlcov/` включена в репозиторий специально для проверки ревьюером без необходимости локального запуска тестов.

После самостоятельно генерации HTML отчета откройте файл htmlcov/index.html в браузере:
```bash
# Сгенерировать новый отчет
pytest tests/ --cov=praktikum.burger --cov-report=html

# Открыть отчет в браузере:
open htmlcov/index.html  # MacOS
start htmlcov/index.html # Windows
xdg-open htmlcov/index.html # Linux
```

**Автор: Ольга Песоцкая**

Курс: Яндекс Практикум, "Инженер по тестированию: от новичка до автоматизатора", 32 когорта

Дата: Декабрь 2025

