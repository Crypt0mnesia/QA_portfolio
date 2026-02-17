import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from urls import ORDER_PAGE_URL

class OrderPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait, ORDER_PAGE_URL)

    @allure.step('Ввести имя: {name}')
    def fill_name(self, name):
        self.set_value(OrderPageLocators.NAME_INPUT, name)

    @allure.step('Ввести фамилию: {surname}')
    def fill_surname(self, surname):
        self.set_value(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step('Ввести адрес: {address}')
    def fill_address(self, address):
        self.set_value(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Ввести телефон: {phone}')
    def fill_phone(self, phone):
        self.set_value(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Открыть dropdown выбора станции метро')
    def open_metro_dropdown(self):
        self.click(OrderPageLocators.METRO_STATION_INPUT)
        self.wait_until_visible(OrderPageLocators.METRO_DROPDOWN)

    @allure.step('Выбрать конкретную станцию: {station_name}')
    def select_specific_station(self, station_name):
        station_locator = (
            OrderPageLocators.METRO_STATION_OPTION[0],
            OrderPageLocators.METRO_STATION_OPTION[1].format(station_name)
        )
        self.scroll_and_click(station_locator)

    @allure.step('Перейти ко второй части формы')
    def go_to_second_part(self):
        self.wait_until_clickable(OrderPageLocators.NEXT_BUTTON)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить дату аренды: {date}')
    def fill_rental_date(self, date):
        self.set_value(OrderPageLocators.DATE_INPUT, date + Keys.ENTER)


    @allure.step('Открыть dropdown выбора срока аренды')
    def open_rental_period_dropdown(self):
        self.click(OrderPageLocators.RENTAL_PERIOD_SELECT)
        self.wait_until_visible(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)

    @allure.step('Выбрать конкретный срок: {rental_period}')
    def select_specific_period(self, rental_period):
        period_locator = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(rental_period)
        )
        self.click_via_js(period_locator)

    @allure.step('Отправить заказ')
    def submit_order(self):
        self.wait_until_clickable(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ в модальном окне')
    def confirm_order(self):
        self.wait_until_visible(OrderPageLocators.CONFIRM_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        self.wait_until_visible(OrderPageLocators.ORDER_NUMBER)
        return self.get_text(OrderPageLocators.ORDER_NUMBER)

    @allure.step('Перейти к статусу заказа')
    def go_to_order_status(self):
        self.click(OrderPageLocators.STATUS_BUTTON)

    @allure.step('Проверить, что открыта страница заказа')
    def should_be_order_page(self):
        self.url_should_contain(ORDER_PAGE_URL)
