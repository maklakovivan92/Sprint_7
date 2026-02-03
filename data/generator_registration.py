import requests
import random
import string

from api.endpoints import *

# Регистрация курьера с обязательными полями
def register_new_courier_and_return_login_password():
    
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    
    response = requests.post(
        CREATE_COURIER,
        json=payload
    )

    return response, login, password, first_name


# Регистрация курьера без логина
def registering_a_new_courier_without_a_login():
    
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "password": password,
        "firstName": first_name
    }

    
    response = requests.post(
        CREATE_COURIER,
        json=payload
    )
    
    return response, password, first_name


# Регистрация курьера без пароля
def registering_a_new_courier_without_a_password():
    
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    
    login = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "firstName": first_name
    }

    
    response = requests.post(
        CREATE_COURIER,
        json=payload
    )
    
    return response, login, first_name