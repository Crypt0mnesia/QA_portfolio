import allure

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

from helpers.urls import MAIN


@allure.feature('Конструктор')
class TestConstructor:

    @allure.title('Переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        order_feed_page.open()
        order_feed_page.click_constructor_button()
        main_page.main_page_loading_wait()
        assert driver.current_url == MAIN

    @allure.title('Переход по клику на раздел «Лента заказов»')
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_feed_button()
        assert "feed" in driver.current_url

    @allure.title('Всплывающее окно при клике на ингредиент')
    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        assert main_page.is_modal_visible() and "Флюоресцентная булка" in main_page.get_modal_ingredient_name()

    @allure.title('Закрытие модального окна крестиком')
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        modal_was_opened = main_page.is_modal_visible()
        main_page.close_modal()
        modal_is_closed = not main_page.is_modal_visible()
        assert modal_was_opened and modal_is_closed

    @allure.title('Увеличение счетчика ингредиента при добавлении в заказ')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        counter_before = main_page.get_counter_value()
        main_page.add_ingredient_to_constructor()
        main_page.wait_for_element(MainPageLocators.COUNTER)
        counter_after = main_page.get_counter_value()
        assert counter_after > counter_before