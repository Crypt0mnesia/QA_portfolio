import pytest
from src.user_api import UserAPI
from src.data_generator import generate_user_data


@pytest.fixture
def registered_user():
    """Зарегистрированный и авторизованный пользователь с токенами"""
    user_api = UserAPI()
    data = generate_user_data()
    email, password, name = data["email"], data["password"], data["name"]

    user_api.register_user(email, password, name)

    login_response = user_api.login_user(email, password)
    login_data = login_response.json()

    access_token = login_data.get("accessToken")
    refresh_token = login_data.get("refreshToken")

    yield email, password, name, access_token, refresh_token

    user_api.logout_user(refresh_token)


