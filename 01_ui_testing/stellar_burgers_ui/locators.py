from selenium.webdriver.common.by import By

class HeaderLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")  # Кнопка "Личный кабинет" в шапке сайта
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")  # Кнопка "Конструктор" в шапке сайта
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип Stellar Burgers

class MainPageLocators:
    """Локаторы главной страницы"""
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт" на главной странице
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  #  Кнопка оформить заказ


class LoginFormLocators:
    """Локаторы формы входа (используются на странице входа)"""
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")  # Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")  # Кнопка "Войти" на странице входа
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")  # Ссылка "Зарегистрироваться" под формой входа
    RECOVERY_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")  # Ссылка "Восстановить пароль" под формой входа


class RegistrationPageLocators:
    """Локаторы страницы регистрации"""
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/../input") # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/../input")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться"
    PASSWORD_ERROR = (By.CSS_SELECTOR, ".input__error")  # Сообщение об ошибке валидации пароля
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]") # Ссылка "Войти" на странице регистрации


class PasswordRecoveryLocators:
    """Локаторы страницы восстановления пароля"""
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]") # Ссылка "Войти" на странице восстановления пароля


class ProfilePageLocators:
    """Локаторы личного кабинета"""
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")  # Кнопка "Выход" в личном кабинете
    PROFILE_SECTION = (By.XPATH, "//a[contains(text(), 'Профиль')]")  # Раздел "Профиль" в личном кабинете (для проверки что мы в ЛК)


class ConstructorLocators:
    """Локаторы конструктора бургеров"""
    BUNS_SECTION = (By.XPATH, "//span[contains(text(), 'Булки')]")  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(), 'Соусы')]")  # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//span[contains(text(), 'Начинки')]")  # Раздел "Начинки
    ACTIVE_SECTION = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")  # Активный раздел конструктора (подсвеченный)

