import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators

from urls import MAIN_PAGE_URL, ORDER_PAGE_URL


class TestMainPage:
    @allure.title('Проверка открытия ответа при клике на вопрос {question_num}')
    @allure.description('Проверяем, что при клике на вопрос отображается соответствующий ответ')
    @pytest.mark.parametrize('question_num, question_locator, answer_locator', [
        (1, MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1),
        (2, MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2),
        (3, MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3),
        (4, MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4),
        (5, MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5),
        (6, MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6),
        (7, MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7),
        (8, MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_8)
    ])
    def test_question_opens_corresponding_answer(self, driver, wait, question_num, question_locator, answer_locator):
        main_page = MainPage(driver, wait)
        main_page.open()

        main_page.scroll_to_element(question_locator)
        main_page.click(question_locator)

        assert main_page.is_visible(answer_locator), f"Ответ на вопрос {question_num} не отображается"

    @allure.title('Проверка перехода на главную через логотип Самоката')
    @allure.description('Проверяем, что клик по логотипу Самоката возвращает на главную страницу')
    def test_scooter_logo_redirect_to_main_page(self, driver, wait):
        main_page = MainPage(driver, wait)
        order_page = OrderPage(driver, wait)

        order_page.open()
        main_page.click_scooter_logo()

        main_page.should_be_main_page()

    @allure.title('Проверка перехода на Дзен через логотип Яндекс')
    @allure.description('Проверяем, что клик по логотипу Яндекс открывает Дзен в новой вкладке')
    def  test_yandex_logo_redirect_to_dzen(self, driver, wait):
        main_page = MainPage(driver, wait)
        main_page.open()

        tabs_before = main_page.get_tabs_count()
        main_page.click_yandex_logo()

        main_page.wait_for_number_of_windows(tabs_before + 1)

        main_page.switch_to_last_tab()
        main_page.wait_until_url_contains('dzen.ru')

        current_url = main_page.get_current_url()
        assert 'dzen.ru' in current_url

    @allure.title('Проверка кнопки заказа вверху страницы')
    @allure.description('Проверяем, что верхняя кнопка "Заказать" ведет на страницу заказа')
    def test_top_order_button_redirect_to_order_page(self, driver, wait):
        main_page = MainPage(driver, wait)
        order_page = OrderPage(driver, wait)

        main_page.open()
        main_page.click_top_order_button()
        order_page.should_be_order_page()

    @allure.title('Проверка кнопки заказа внизу страницы')
    @allure.description('Проверяем, что нижняя кнопка "Заказать" ведет на страницу заказа')
    def test_bottom_order_button_redirect_to_order_page(self, driver, wait):
        main_page = MainPage(driver, wait)
        order_page = OrderPage(driver, wait)

        main_page.open()

        main_page.click_bottom_order_button()
        order_page.should_be_order_page()