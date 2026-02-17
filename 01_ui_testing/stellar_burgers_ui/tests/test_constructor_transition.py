import pytest
from selenium.webdriver.support import expected_conditions as EC

from urls import MAIN
from locators import MainPageLocators, HeaderLocators


class TestConstructorTransition:
    """Тесты переходов из личного кабинета в конструктор"""
    def test_go_to_constructor_from_account_via_constructor_button(self, wait, authenticated_user):
        driver = authenticated_user

        personal_account_button = wait.until(EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()

        constructor_button = wait.until(EC.element_to_be_clickable(HeaderLocators.CONSTRUCTOR_BUTTON))
        constructor_button.click()

        order_button = wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))

        assert order_button.is_displayed()
        assert driver.current_url == MAIN


    def test_go_to_constructor_from_account_via_logo(self, authenticated_user,wait):
        driver = authenticated_user

        personal_account_button = wait.until(EC.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button.click()

        logo = wait.until(EC.element_to_be_clickable(HeaderLocators.LOGO))
        logo.click()

        order_button = wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))

        assert order_button.is_displayed()
        assert driver.current_url == MAIN
