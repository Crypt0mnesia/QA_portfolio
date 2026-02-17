import allure

from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from urls import MAIN_PAGE_URL

class MainPage(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait, MAIN_PAGE_URL)

    @allure.step('Клик по верхней кнопке "Заказать"')
    def click_top_order_button(self):
        self.click(BasePageLocators.TOP_ORDER_BUTTON)

    @allure.step('Клик по нижней кнопке "Заказать"')
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_via_js(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step('Клик по вопросу и получение ответа')
    def get_answer_text(self, question_locator, answer_locator):
        self.scroll_and_click(question_locator)
        return self.get_text(answer_locator)

    @allure.step('Клик по логотипу Яндекс')
    def click_yandex_logo(self):
        self.click(BasePageLocators.YANDEX_LOGO)

    @allure.step('Клик по логотипу Самокат')
    def click_scooter_logo(self):
        self.click(BasePageLocators.SCOOTER_LOGO)

    @allure.step('Проверить, что открыта главная страница')
    def should_be_main_page(self):
        self.url_should_contain(MAIN_PAGE_URL)
