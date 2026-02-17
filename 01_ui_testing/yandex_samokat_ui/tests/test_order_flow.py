import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage

from helper import generate_order_data
from urls import ORDER_PAGE_URL, TRACK_PAGE_URL

class TestOrderFlow:
    @allure.title('Позитивный сценарий заказа с точкой входа: {entry_point}')
    @pytest.mark.parametrize('entry_point, order_data', [
        ('top', generate_order_data()),
        ('bottom', generate_order_data())
    ])
    def test_successful_order_complete_flow(self, driver, wait, entry_point, order_data):
        main_page = MainPage(driver, wait)
        order_page = OrderPage(driver, wait)

        main_page.open()

        click_methods = {
            'top': main_page.click_top_order_button,
            'bottom': main_page.click_bottom_order_button
        }
        click_methods[entry_point]()

        order_page.wait_until_url_contains(ORDER_PAGE_URL)

        order_page.fill_name(order_data['name'])
        order_page.fill_surname(order_data['surname'])
        order_page.fill_address(order_data['address'])
        order_page.fill_phone(order_data['phone'])
        order_page.open_metro_dropdown()
        order_page.select_specific_station(order_data['metro_station'])
        order_page.go_to_second_part()

        order_page.fill_rental_date(order_data['date'])
        order_page.open_rental_period_dropdown()
        order_page.select_specific_period(order_data['rental_period'])
        order_page.submit_order()

        order_page.confirm_order()

        order_number = order_page.get_order_number()
        assert order_number is not None
        assert order_number.strip() != ""
