import requests
import random
import string
from api.endpoints import *

# Авторизация курьера с обязательными полями
def courier_authorization_with_required_fields(login, password):
    payload = {
        "login": login,
        "password": password,
    }
    response = requests.post(
        LOGIN_COURIER,
        json=payload
    )

    return response


# Авторизация курьера без логина
def courier_authorization_without_login(password):
    payload = {
        "password": password
    }
    response = requests.post(
        LOGIN_COURIER,
        json=payload
    )

    return response


# Авторизация курьера без пароля
def courier_authorization_without_password(login):
    payload = {
        "login": login
    }
    response = requests.post(
        LOGIN_COURIER,
        json=payload
    )

    return response


# Генерация рандомного логина или пароля
def generate_random_login_or_password(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))