import allure

from api.endpoints import *
from api.body_response import *
from conftest import *
from helpers import *

class TestCourierAuthorization:

    @allure.title("Курьер может авторизоваться")
    def test_courier_authorization(self, new_courier):        
        response, login, password, first_name = new_courier
        authorization_response = courier_authorization_with_required_fields(login, password)
    
        assert authorization_response.status_code == successful_authorization_code
        body = authorization_response.json()
        assert authorization_id_key in body
        id_courier = authorization_response.json()['id']
        assert body[authorization_id_key] == id_courier


    @allure.title("Курьер не может авторизоваться, если не передан логин")
    def test_courier_authorization_without_login(self, new_courier):        
        response, login, password, first_name = new_courier

        authorization_response = courier_authorization_without_login(password)
    
        assert authorization_response.status_code == courier_authorization_code_without_required_fields
        assert authorization_response.json() == courier_authorization_body_without_required_fields



    @allure.title("Курьер не может авторизоваться, если не передан пароль")
    def test_courier_authorization_without_password(self, new_courier):        
        response, login, password, first_name = new_courier
        authorization_response = courier_authorization_without_password(login)
    
        assert authorization_response.status_code == courier_authorization_code_without_required_fields
        assert authorization_response.json() == courier_authorization_body_without_required_fields


    @allure.title("Курьер не может авторизоваться с неправильным логином")
    def test_courier_authorization_with_a_bad_login(self, new_courier):        
        response, login, password, first_name = new_courier
        login_bad = generate_random_string(10)
        authorization_response = courier_authorization_with_required_fields(login_bad, password)

        assert authorization_response.status_code == authorization_code_for_a_non_existent_user
        assert authorization_response.json() == authorization_body_for_a_non_existent_user
        

    @allure.title("Курьер не может авторизоваться с неправильным паролем")
    def test_courier_authorization_with_a_bad_password(self, new_courier):        
        response, login, password, first_name = new_courier
        password_bad = generate_random_string(10)
        authorization_response = courier_authorization_with_required_fields(login, password_bad)

        assert authorization_response.status_code == authorization_code_for_a_non_existent_user
        assert authorization_response.json() == authorization_body_for_a_non_existent_user


    @allure.title("Авторизации несуществующего курьера")
    def test_authorization_of_a_non_existent_courier(self):
        
        authorization_response = authorization_of_a_non_existent_courier()

        assert authorization_response.status_code == authorization_code_for_a_non_existent_user
        assert authorization_response.json() == authorization_body_for_a_non_existent_user
        
