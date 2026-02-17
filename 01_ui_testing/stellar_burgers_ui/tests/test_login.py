import pytest
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from urls import MAIN, REGISTER, FORGOT_PASSWORD
from locators import MainPageLocators, HeaderLocators, LoginFormLocators, RegistrationPageLocators, PasswordRecoveryLocators
from helpers import login_user


class TestLogin:
    """Тесты функциональности входа"""

    def test_login_via_main_page_button(self, driver, wait):
        """Вход через кнопку 'Войти в аккаунт' на главной странице"""
        driver.get(MAIN)

        login_account_button = wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON))
        driver.execute_script("arguments[0].click();",login_account_button)

        wait.until(EC.presence_of_element_located(LoginFormLocators.EMAIL_INPUT))

        login_user(driver, wait, Credentials.EMAIL,Credentials.PASSWORD)

        order_button = wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))

        assert order_button.is_displayed()
        assert driver.current_url == MAIN

    def test_login_via_personal_account_button(self, driver, wait):
        """Вход через кнопку 'Личный кабинет'"""
        driver.get(MAIN)

        personal_account_button = wait.until(EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.execute_script("arguments[0].click();", personal_account_button)

        wait.until(EC.presence_of_element_located(LoginFormLocators.EMAIL_INPUT))

        login_user(driver, wait, Credentials.EMAIL, Credentials.PASSWORD)

        order_button = wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))

        assert order_button.is_displayed()
        assert driver.current_url == MAIN

    def test_login_via_registration_form(self, driver, wait):
        """Вход через кнопку в форме регистрации"""
        driver.get(REGISTER)

        login_link = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK))
        driver.execute_script("arguments[0].click();", login_link)

        wait.until(EC.presence_of_element_located(LoginFormLocators.EMAIL_INPUT))

        login_user(driver, wait, Credentials.EMAIL, Credentials.PASSWORD)

        order_button = wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))

        assert order_button.is_displayed()
        assert driver.current_url == MAIN

    def test_login_via_password_recovery_form(self, driver, wait):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(FORGOT_PASSWORD)

        login_link = wait.until(EC.element_to_be_clickable(PasswordRecoveryLocators.LOGIN_LINK))
        driver.execute_script("arguments[0].click();", login_link)

        wait.until(EC.presence_of_element_located(LoginFormLocators.EMAIL_INPUT))

        login_user(driver, wait, Credentials.EMAIL, Credentials.PASSWORD)

        order_button = wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))

        assert order_button.is_displayed()
        assert driver.current_url == MAIN