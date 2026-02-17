import allure
from pages.base_page import BasePage
from locators.auth_locators import AuthLocators
from helpers.urls import LOGIN


class LoginPage(BasePage):

    @allure.step('Открыть страницу авторизации')
    def open(self):
        self.driver.get(LOGIN)
        self.wait_for_element(AuthLocators.EMAIL_INPUT)

    @allure.step('Авторизоваться')
    def login(self, email, password):
        self.input_text(AuthLocators.EMAIL_INPUT, email)
        self.input_text(AuthLocators.PASSWORD_INPUT, password)
        self.click(AuthLocators.LOGIN_BUTTON)