from faker import Faker
import random
from data import COHORT

fake = Faker()


def generate_user_data():
    name = fake.first_name()
    email = f"{name}_{COHORT}_{random.randint(100, 999)}@yandex.ru"
    password = fake.password(length=10)

    return {
        "name": f"{name}",
        "email": email,
        "password": password
    }