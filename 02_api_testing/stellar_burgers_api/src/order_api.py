import allure
from src.base_api import BaseAPI
from src.endpoints import ORDERS


class OrderAPI(BaseAPI):
    @allure.step("Создать заказ")
    def create_order(self, ingredients):
        payload = {"ingredients": ingredients}
        return self.post(ORDERS, payload)
