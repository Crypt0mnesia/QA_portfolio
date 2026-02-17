import pytest
from selenium.webdriver.support import expected_conditions as EC

from generator import generate_user_data
from data import TextMessages
from urls import LOGIN, REGISTER
from locators import RegistrationPageLocators, LoginFormLocators


class TestRegistration:
    """Тесты функциональности регистрации"""

    def test_successful_registration(self, driver, wait):
        """Тест успешной регистрации"""
        user = generate_user_data()

        driver.get(REGISTER)

        name_input = wait.until(EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))
        name_input.send_keys(user["name"])

        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(user["email"])

        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_input.send_keys(user["password"])

        register_button = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON))
        driver.execute_script("arguments[0].click();", register_button)

        wait.until(EC.element_to_be_clickable(LoginFormLocators.LOGIN_BUTTON))

        # Проверяем URL
        assert driver.current_url == LOGIN

    def test_registration_short_password_error(self, driver, wait):
        """Ошибка при регистрации с паролем длиной 5 символов"""
        user = generate_user_data()
        user["password"] = "12345"  # 5 символов

        driver.get(REGISTER)

        name_input = wait.until(EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT))
        name_input.send_keys(user["name"])

        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(user["email"])

        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_input.send_keys(user["password"])

        register_button = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON))
        driver.execute_script("arguments[0].click();", register_button)

        # Ждем появления ошибки и проверяем что остались на странице регистрации
        error_element = wait.until(EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_ERROR))

        # Проверяем текст ошибки и URL
        assert TextMessages.PASSWORD_ERROR in error_element.text
        assert driver.current_url == REGISTER