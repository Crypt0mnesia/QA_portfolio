import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from helpers.urls import FEED
from helpers.data import LONG_TIMEOUT

class OrderFeedPage(BasePage):

    @allure.step('Открыть ленту заказов')
    def open(self):
        self.driver.get(FEED)
        self.wait_for_page_load()

    @allure.step('Получить счетчик "Выполнено за все время"')
    def get_total_counter(self):
        text = self.get_text(OrderFeedLocators.TOTAL_COUNTER)
        return int(text)

    @allure.step('Получить счетчик "Выполнено за сегодня"')
    def get_today_counter(self):
        if self.is_visible(OrderFeedLocators.TODAY_COUNTER):
            text = self.get_text(OrderFeedLocators.TODAY_COUNTER)
            return int(text) if text.isdigit() else 0
        return 0


    @allure.step('Нажать "Конструктор" в шапке')
    def click_constructor_button(self):
        self.click(HeaderLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Дождаться загрузки страницы ленты заказов')
    def wait_for_page_load(self):
        self.wait_for_overlay_to_disappear(MainPageLocators.OVERLAY)
        self.wait_for_element(OrderFeedLocators.PAGE_TITLE, timeout=LONG_TIMEOUT)

    @allure.step('Проверить наличие заказа в работе')
    def is_order_in_progress(self, order_number):
        self.wait_for_element(OrderFeedLocators.ORDERS_IN_PROGRESS, timeout=LONG_TIMEOUT)
        elements = self.get_all_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
        for element in elements:
            if element.text.strip() == order_number:
                return True
        return False