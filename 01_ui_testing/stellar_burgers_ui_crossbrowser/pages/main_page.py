import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.header_locators import HeaderLocators
from helpers.urls import MAIN
from helpers.data import LONG_TIMEOUT


class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open(self):
        self.driver.get(MAIN)
        self.main_page_loading_wait()

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_overlay_to_disappear(MainPageLocators.OVERLAY)
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_TITLE, timeout=LONG_TIMEOUT)

    @allure.step('Нажать кнопку "Войти в аккаунт"')
    def click_login_account_button(self):
        self.safe_click(MainPageLocators.LOGIN_ACCOUNT_BUTTON)

    @allure.step('Кликнуть на ингредиент')
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    @allure.step('Проверить видимость модального окна')
    def is_modal_visible(self):
        return self.is_visible(MainPageLocators.MODAL)

    @allure.step('Получить название ингредиента в модальном окне')
    def get_modal_ingredient_name(self):
        return self.get_text(MainPageLocators.MODAL_INGREDIENT_NAME)

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE)
        self.wait_for_element_hide(MainPageLocators.MODAL)

    @allure.step('Добавить ингредиент в конструктор')
    def add_ingredient_to_constructor(self):
        self.wait_for_presence(MainPageLocators.CONSTRUCTOR_AREA)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT, MainPageLocators.CONSTRUCTOR_AREA)

    @allure.step('Получить значение счетчика')
    def get_counter_value(self):
        text = self.get_text(MainPageLocators.COUNTER)
        return int(text)

    @allure.step('Оформить заказ')
    def make_order(self):
        self.add_ingredient_to_constructor()
        self.click(MainPageLocators.ORDER_BUTTON)
        self.wait_for_element(MainPageLocators.MODAL)
        self.wait_for_order_number_ready()
        order_number = self.get_order_number_from_modal()
        self.close_modal()
        return order_number

    @allure.step('Дождаться оформления с номером заказа')
    def wait_for_order_number_ready(self):
        return self.wait_for_custom_condition(
            lambda d: len(self.get_text(MainPageLocators.MODAL_ORDER_NUMBER)) == 6,
            timeout=LONG_TIMEOUT
        )

    @allure.step('Получить номер заказа из модального окна')
    def get_order_number_from_modal(self):
        text = self.get_text(MainPageLocators.MODAL_ORDER_NUMBER)
        return f"0{text}"

    @allure.step('Нажать "Лента заказов" в шапке')
    def click_order_feed_button(self):
        self.click(HeaderLocators.ORDER_FEED_BUTTON)


