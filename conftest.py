import requests
import pytest
import allure
from api.endpoints import *
from helpers import *
from api.body_response import *

# Создание и удаление после теста курьера
@pytest.fixture
def new_courier():
    with allure.step("Создать курьера"):
        payload = generate_payload_login_password_firstname()
        create_response = requests.post(CREATE_COURIER, json=payload)

        login = payload["login"]
        password = payload["password"]
        first_name = payload["firstName"]

    yield create_response, login, password, first_name

    with allure.step("Удалить курьера"):
        auth_payload = {"login": login, "password": password}
        auth_response = requests.post(LOGIN_COURIER, json=auth_payload)

        if auth_response.status_code == successful_authorization_code and authorization_id_key in auth_response.json():
            courier_id = auth_response.json()["id"]
            requests.delete(f"{COURIER_REMOVAL}/{courier_id}")


@allure.step("Авторизовать курьера с обязательными полями")
def courier_authorization_with_required_fields(login, password):
    payload = {"login": login, "password": password,}
    response = requests.post(LOGIN_COURIER, json=payload)
    return response


@allure.step("Авторизовать курьера без логина")
def courier_authorization_without_login(password):
    payload = {"password": password}
    response = requests.post(LOGIN_COURIER, json=payload)
    return response


@allure.step("Авторизовать курьера без пароля")
def courier_authorization_without_password(login):
    payload = {"login": login}
    response = requests.post(LOGIN_COURIER, json=payload)
    return response


@allure.step("Авторизовать несуществующего курьера")   
def authorization_of_a_non_existent_courier():    
    payload = generate_payload_login_password()    
    response = requests.post(LOGIN_COURIER, json=payload)
    return response


@allure.step("Зарегистрировать курьера без логина")   
def registering_a_new_courier_without_a_login():   
    payload = generate_payload_password_firstname()  
    response = requests.post(CREATE_COURIER, json=payload)
    password = payload["password"]
    first_name = payload["firstName"]  
    return response, password, first_name


@allure.step("Зарегистрировать курьера без пароля")   
def registering_a_new_courier_without_a_password():
    payload = generate_payload_login_firstname()   
    response = requests.post(CREATE_COURIER, json=payload)
    login = payload["login"]
    first_name = payload["firstName"]   
    return response, login, first_name


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
