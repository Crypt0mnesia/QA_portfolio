class Credentials:
    """Учетные данные зарегистрированного пользователя"""
    EMAIL = "Olga_32_132@yandex.ru"
    PASSWORD = "qwerty1234"

class TextMessages:
    """Текстовые элементы приложения"""
    PASSWORD_ERROR = "Некорректный пароль"   # Ошибка валидации пароля
    LOGIN_BUTTON = "Войти"                   # Текст кнопки входа
    REGISTER_BUTTON = "Зарегистрироваться"   # Текст кнопки регистрации

    # Разделы конструктора
    BUNS = "Булки"
    SAUCES = "Соусы"
    FILLINGS = "Начинки"


class Settings:
    """Настройки приложения"""
    WINDOW_WIDTH = 1366       # Ширина окна браузера
    WINDOW_HEIGHT = 768       # Высота окна браузера
    DEFAULT_TIMEOUT = 30      # Стандартное время ожидания
    MIN_PASSWORD_LENGTH = 6   # Минимальная длина пароля


# Номер когорты для генерации email
COHORT = "32"