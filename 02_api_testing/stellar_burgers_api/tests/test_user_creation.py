import allure
from src.user_api import UserAPI
from src.data import ExpectedResponses, ResponseMessages
from src.data_generator import generate_user_data


@allure.epic("Stellar Burgers API")
@allure.feature("Создание пользователя")
class TestUserCreation:

    @allure.story("Создать уникального пользователя")
    @allure.title("Успешная регистрация нового пользователя")
    def test_create_unique_user_success(self):
        user_api = UserAPI()
        user_data = generate_user_data()

        with allure.step("Зарегистрировать нового пользователя с валидными данными"):
            response = user_api.register_user(
                user_data["email"],
                user_data["password"],
                user_data["name"]
            )

        response_body = response.json()

        with allure.step("Проверить успешную регистрацию: код 200, токены и данные пользователя"):
            assert response.status_code == ExpectedResponses.SUCCESSFUL_REGISTRATION[0]
            assert response_body["success"] is True
            assert "accessToken" in response_body
            assert "refreshToken" in response_body
            assert "user" in response_body
            assert response_body["user"]["email"] == user_data["email"]
            assert response_body["user"]["name"] == user_data["name"]

    @allure.story("Создать пользователя, который уже зарегистрирован")
    @allure.title("Неуспешная регистрация: пользователь уже существует")
    def test_create_existing_user_fails(self, registered_user):
        user_api = UserAPI()
        email, password, name, _, _ = registered_user

        with allure.step("Попытаться повторно зарегистрировать существующего пользователя"):
            response = user_api.register_user(email, password, name)

        response_body = response.json()

        with allure.step("Проверить ошибку 403: пользователь уже существует"):
            assert response.status_code == ExpectedResponses.USER_ALREADY_EXISTS[0]
            assert response_body == ResponseMessages.USER_EXISTS

    @allure.story("Создать пользователя без обязательных полей")
    @allure.title("Неуспешная регистрация: отсутствует email")
    def test_create_user_without_email_fails(self):
        user_api = UserAPI()
        user_data = generate_user_data()

        with allure.step("Попытаться зарегистрировать пользователя без email"):
            response = user_api.register_user("", user_data["password"], user_data["name"])

        response_body = response.json()

        with allure.step("Проверить ошибку 403: обязательные поля не заполнены"):
            assert response.status_code == ExpectedResponses.MISSING_REGISTRATION_FIELDS[0]
            assert response_body == ResponseMessages.MISSING_FIELDS

    @allure.story("Создать пользователя без обязательных полей")
    @allure.title("Неуспешная регистрация: отсутствует пароль")
    def test_create_user_without_password_fails(self):
        user_api = UserAPI()
        user_data = generate_user_data()

        with allure.step("Попытаться зарегистрировать пользователя без пароля"):
            response = user_api.register_user(user_data["email"], "", user_data["name"])

        response_body = response.json()

        with allure.step("Проверить ошибку 403: обязательные поля не заполнены"):
            assert response.status_code == ExpectedResponses.MISSING_REGISTRATION_FIELDS[0]
            assert response_body == ResponseMessages.MISSING_FIELDS

    @allure.story("Создать пользователя без обязательных полей")
    @allure.title("Неуспешная регистрация: отсутствует имя")
    def test_create_user_without_name_fails(self):
        user_api = UserAPI()
        user_data = generate_user_data()

        with allure.step("Попытаться зарегистрировать пользователя без имени"):
            response = user_api.register_user(user_data["email"], user_data["password"], "")

        response_body = response.json()

        with allure.step("Проверить ошибку 403: обязательные поля не заполнены"):
            assert response.status_code == ExpectedResponses.MISSING_REGISTRATION_FIELDS[0]
            assert response_body == ResponseMessages.MISSING_FIELDS