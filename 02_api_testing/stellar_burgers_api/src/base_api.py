import json
import requests
import allure


class BaseAPI:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.auth_token = None

    def set_auth_token(self, token):
        self.auth_token = token
        if token:
            if token.startswith('Bearer '):
                clean_token = token
            else:
                clean_token = f"Bearer {token}"
            self.headers['Authorization'] = clean_token
        elif 'Authorization' in self.headers:
            del self.headers['Authorization']

    @allure.step("POST запрос к {endpoint}")
    def post(self, endpoint, payload):
        data = json.dumps(payload) if payload else None
        return requests.post(endpoint, data=data, headers=self.headers)

    @allure.step("GET запрос к {endpoint}")
    def get(self, endpoint, params=None):
        return requests.get(endpoint, params=params, headers=self.headers)

