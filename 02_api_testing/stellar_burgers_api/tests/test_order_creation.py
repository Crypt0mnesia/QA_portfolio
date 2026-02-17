import allure
from src.order_api import OrderAPI
from src.data import ExpectedResponses, ResponseMessages, TestData


@allure.epic("Stellar Burgers API")
@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.story("Создание заказа с авторизацией")
    @allure.title("Успешное создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, registered_user):
        order_api = OrderAPI()
        _, _, _, access_token, _ = registered_user
        order_api.set_auth_token(access_token)

        with allure.step("Создать заказ с валидными ингредиентами"):
            response = order_api.create_order(TestData.TEST_INGREDIENT_IDS[:2])

        response_body = response.json()

        with allure.step("Проверить успешное создание заказа: код 200 и номер заказа"):
            assert response.status_code == ExpectedResponses.SUCCESSFUL_ORDER_CREATION[0]
            assert response_body["success"] is True
            assert "order" in response_body
            assert "number" in response_body["order"]
            assert isinstance(response_body["order"]["number"], int)

    @allure.story("Создание заказа без авторизации")
    @allure.title("Особый случай: создание заказа без авторизации")
    def test_create_order_without_auth(self):
        order_api = OrderAPI()
        order_api.set_auth_token(None)

        with allure.step("Попытаться создать заказ без токена авторизации"):
            response = order_api.create_order(TestData.TEST_INGREDIENT_IDS[:2])

        response_body = response.json()

        with allure.step("Проверить успешное создание заказа без авторизации"):
            assert response.status_code == ExpectedResponses.SUCCESSFUL_ORDER_CREATION[0]
            assert response_body["success"] is True
            assert "name" in response_body
            assert "order" in response_body
            assert "number" in response_body["order"]

    @allure.story("Создание заказа с ингредиентами")
    @allure.title("Успешное создание заказа с одним ингредиентом")
    def test_create_order_with_one_ingredient(self, registered_user):
        order_api = OrderAPI()
        _, _, _, access_token, _ = registered_user
        order_api.set_auth_token(access_token)

        with allure.step("Создать заказ с одним ингредиентом - булка"):
            response = order_api.create_order([TestData.TEST_INGREDIENT_IDS[0]])

        response_body = response.json()

        with allure.step("Проверить успешное создание заказа: код 200"):
            assert response.status_code == ExpectedResponses.SUCCESSFUL_ORDER_CREATION[0]
            assert response_body["success"] is True

    @allure.story("Создание заказа без ингредиентов")
    @allure.title("Неуспешное создание заказа: пустой список ингредиентов")
    def test_create_order_without_ingredients(self, registered_user):
        order_api = OrderAPI()
        _, _, _, access_token, _ = registered_user
        order_api.set_auth_token(access_token)

        with allure.step("Попытаться создать заказ без ингредиентов (пустой список)"):
            response = order_api.create_order([])

        response_body = response.json()

        with allure.step("Проверить ошибку 400: ингредиенты обязательны"):
            assert response.status_code == ExpectedResponses.ORDER_WITHOUT_INGREDIENTS[0]
            assert response_body == ResponseMessages.INGREDIENTS_REQUIRED

    @allure.story("Создание заказа с неверным хешем ингредиентов")
    @allure.title("Неуспешное создание заказа: невалидный хеш ингредиента")
    def test_create_order_with_invalid_ingredient(self, registered_user):
        order_api = OrderAPI()
        _, _, _, access_token, _ = registered_user
        order_api.set_auth_token(access_token)

        with allure.step("Попытаться создать заказ с невалидным хешем ингредиента"):
            response = order_api.create_order([TestData.INVALID_INGREDIENT_IDS[0]])

        with allure.step("Проверить ошибку 500: внутренняя ошибка сервера"):
            assert response.status_code == ExpectedResponses.ORDER_INVALID_INGREDIENT[0]

    @allure.story("Создание заказа с ингредиентами")
    @allure.title("Успешное создание заказа с несколькими ингредиентами")
    def test_create_order_with_multiple_ingredients(self, registered_user):
        order_api = OrderAPI()
        _, _, _, access_token, _ = registered_user
        order_api.set_auth_token(access_token)

        with allure.step("Создать заказ с несколькими валидными ингредиентами"):
            response = order_api.create_order(TestData.TEST_INGREDIENT_IDS[:3])

        response_body = response.json()

        with allure.step("Проверить успешное создание заказа: код 200"):
            assert response.status_code == ExpectedResponses.SUCCESSFUL_ORDER_CREATION[0]
            assert response_body["success"] is True