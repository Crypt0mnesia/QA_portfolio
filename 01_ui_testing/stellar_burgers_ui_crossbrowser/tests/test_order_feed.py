import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage



@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title('Увеличение счетчика "Выполнено за все время" при создании заказа')
    def test_total_counter_increases(self, authenticated_user):
        main_page = MainPage(authenticated_user)
        order_feed_page = OrderFeedPage(authenticated_user)

        order_feed_page.open()
        total_before = order_feed_page.get_total_counter()
        order_feed_page.click_constructor_button()
        main_page.main_page_loading_wait()
        main_page.make_order()
        order_feed_page.open()
        assert order_feed_page.get_total_counter() > total_before

    @allure.title('Увеличение счетчика "Выполнено за сегодня" при создании заказа')
    def test_today_counter_increases(self, authenticated_user):
        main_page = MainPage(authenticated_user)
        order_feed_page = OrderFeedPage(authenticated_user)

        order_feed_page.open()
        today_before = order_feed_page.get_today_counter()

        order_feed_page.click_constructor_button()
        main_page.main_page_loading_wait()
        main_page.make_order()

        order_feed_page.open()
        assert order_feed_page.get_today_counter() > today_before

    @allure.title('Появление номера заказа в разделе "В работе"')
    def test_order_appears_in_progress(self, authenticated_user):
        main_page = MainPage(authenticated_user)
        order_feed_page = OrderFeedPage(authenticated_user)

        order_number = main_page.make_order()
        order_feed_page.open()
        assert order_feed_page.is_order_in_progress(order_number)