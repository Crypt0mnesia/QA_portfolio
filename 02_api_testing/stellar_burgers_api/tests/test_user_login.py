import allure
from src.user_api import UserAPI
from src.data import ExpectedResponses, ResponseMessages
from src.data_generator import generate_user_data


@allure.epic("Stellar Burgers API")
@allure.feature("Логин пользователя")
class TestUserLogin:

    @allure.story("Вход под существующим пользователем")
    @allure.title("Успешная авторизация существующего пользователя")
    def test_login_existing_user_success(self, registered_user):
        user_api = UserAPI()
        email, password, _, _, _ = registered_user

        with allure.step("Авторизоваться под существующим пользователем"):
            response = user_api.login_user(email, password)

        response_body = response.json()

        with allure.step("Проверить успешную авторизацию: код 200, токены и данные пользователя"):
            assert response.status_code == ExpectedResponses.SUCCESSFUL_LOGIN[0]
            assert response_body["success"] is True
            assert "accessToken" in response_body
            assert "refreshToken" in response_body
            assert "user" in response_body
            assert response_body["user"]["email"] == email

    @allure.story("Вход с неверным логином и паролем")
    @allure.title("Неуспешная авторизация: неверные учетные данные")
    def test_login_with_invalid_credentials_fails(self):
        user_api = UserAPI()
        user_data = generate_user_data()
        wrong_email = user_data["email"]
        wrong_password = user_data["password"]

        with allure.step("Попытаться авторизоваться с неверными email и паролем"):
            response = user_api.login_user(wrong_email, wrong_password)

        response_body = response.json()

        with allure.step("Проверить ошибку 401: неверные учетные данные"):
            assert response.status_code == ExpectedResponses.INVALID_LOGIN_CREDENTIALS[0]
            assert response_body == ResponseMessages.INVALID_CREDENTIALS
