import requests
import allure
from api.endpoints import *
from helpers import *

@allure.step("Авторизовать курьера с обязательными полями")
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


@allure.step("Авторизовать курьера без логина")
def courier_authorization_without_login(password):
    payload = {
        "password": password
    }
    response = requests.post(
        LOGIN_COURIER,
        json=payload
    )

    return response


@allure.step("Авторизовать курьера без пароля")
def courier_authorization_without_password(login):
    payload = {
        "login": login
    }
    response = requests.post(
        LOGIN_COURIER,
        json=payload
    )

    return response


@allure.step("Авторизовать несуществующего курьера")
def authorization_of_a_non_existent_courier():
    payload = {
        "login": generate_random_string(10),
        "password": generate_random_string(10)
    }
    response = requests.post(
        LOGIN_COURIER,
        json=payload
    )

    return response




@allure.step("Зарегистрировать курьера с обязательными полями")
def register_new_courier_and_return_login_password():
    
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


@allure.step("Зарегистрировать курьера без логина")
def registering_a_new_courier_without_a_login():
    
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


@allure.step("Зарегистрировать курьера без пароля")
def registering_a_new_courier_without_a_password():
 
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



@allure.step("Удалить курьера в системе")
def courier_removal(login, password):
    payload = {
        "login": login,
        "password": password
    }
    
    response = requests.post(
    LOGIN_COURIER,
    json=payload
    )
    
    id_courier = response.json()['id']
    requests.delete(f"{COURIER_REMOVAL}{id_courier}")


@allure.step("Получить список заказов")
def get_a_list_of_orders():
    response = requests.get(GET_ORDERS_LIST)
    response_json = response.json()
    return response_json


@allure.step("Создаём заказ с цветом самоката")
def create_order_with_color_variants(payload):
    return requests.post(CREATE_ORDER, json=payload)


@allure.step("Создаём дублирующего курьера")
def duplicate_courier(payload):
    return requests.post(CREATE_COURIER, json=payload)
