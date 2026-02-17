import allure
from src.base_api import BaseAPI
from src.endpoints import REGISTER, LOGIN, LOGOUT

class UserAPI(BaseAPI):

    def __init__(self):
        super().__init__()
        self.refresh_token = None

    @allure.step("Зарегистрировать пользователя")
    def register_user(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = self.post(REGISTER, payload)

        if response.status_code == 200 and response.json().get("success"):
            data = response.json()
            access_token = data.get("accessToken")
            self.set_auth_token(access_token)
            self.refresh_token = data.get("refreshToken")

        return response

    @allure.step("Авторизовать пользователя")
    def login_user(self, email, password):
        payload = {
            "email": email,
            "password": password
        }
        response = self.post(LOGIN, payload)

        if response.status_code == 200 and response.json().get("success"):
            data = response.json()
            access_token = data.get("accessToken")
            self.set_auth_token(access_token)
            self.refresh_token = data.get("refreshToken")

        return response

    @allure.step("Выйти из системы")
    def logout_user(self, refresh_token=None):
        if refresh_token is None:
            refresh_token = self.refresh_token

        payload = {"token": refresh_token}
        response = self.post(LOGOUT, payload)
        self.set_auth_token(None)
        self.refresh_token = None
        return response

