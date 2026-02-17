import random
import string
import time


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_unique_email():
    timestamp = int(time.time() * 1000)
    random_part = generate_random_string(5)
    return f"user_{timestamp}_{random_part}@test.com"


def generate_user_data():
    return {
        "email": generate_unique_email(),
        "password": generate_random_string(10),
        "name": generate_random_string(8)
    }

