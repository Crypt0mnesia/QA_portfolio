from faker import Faker
from data import TestData

fake = Faker('ru_RU')

def generate_order_data():
    """Генерация данных для заказа самоката"""
    return {
        'name': fake.first_name(),
        'surname': fake.last_name(),
        'address': fake.street_name() + ' ' + str(fake.random_int(min=1, max=200)),
        'metro_station': fake.random_element(TestData.METRO_STATIONS),
        'phone': fake.numerify('+7##########'),
        'date': fake.future_date().strftime('%d.%m.%Y'),
        'rental_period': fake.random_element(TestData.RENTAL_PERIODS)
    }

