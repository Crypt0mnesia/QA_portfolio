import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from data import Settings, Credentials
from urls import MAIN, LOGIN
from locators import LoginFormLocators, MainPageLocators


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера"""
    driver = webdriver.Chrome()
    driver.set_window_size(Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT)
    driver.get(MAIN)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    """Фикстура для использования явных ожиданий в тестах"""
    return WebDriverWait(driver, Settings.DEFAULT_TIMEOUT)


@pytest.fixture
def authenticated_user(driver, wait):
    """Фикстура для входа с использованием данных зарегистрированного пользователя"""

    # Заполняем форму входа
    driver.get(LOGIN)
    email_input = wait.until(EC.presence_of_element_located(LoginFormLocators.EMAIL_INPUT))
    email_input.send_keys(Credentials.EMAIL)

    password_input = driver.find_element(*LoginFormLocators.PASSWORD_INPUT)
    password_input.send_keys(Credentials.PASSWORD)

    login_button = wait.until(EC.element_to_be_clickable(LoginFormLocators.LOGIN_BUTTON))
    login_button.click()

    # Ждем завершения входа
    wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))

    return driver
