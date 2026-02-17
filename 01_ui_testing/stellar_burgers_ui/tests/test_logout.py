import pytest
from selenium.webdriver.support import expected_conditions as EC

from urls import LOGIN
from locators import HeaderLocators, ProfilePageLocators, LoginFormLocators

class TestLogout:
    """Тест выхода из аккаунта по кнопке "Выйти" в личном кабинете"""
    def test_logout(self, authenticated_user, wait):

        driver = authenticated_user

        personal_account_button = wait.until(EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()

        logout_button = wait.until(EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON))
        logout_button.click()

        login_button = wait.until(EC.presence_of_element_located(LoginFormLocators.LOGIN_BUTTON))

        assert login_button.is_displayed()
        assert driver.current_url == LOGIN