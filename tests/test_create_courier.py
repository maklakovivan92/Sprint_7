import allure

from api.endpoints import *
from api.body_response import *
from conftest import *


class TestCreatingACourier:

    @allure.title("Создание курьера")
    def test_create_courier_success(self):
        response, login, password, first_name = (
            register_new_courier_and_return_login_password()
        )

        assert response.status_code == code_for_successful_courier_creation
        assert response.json() == the_body_of_a_successfully_created_courier

        courier_removal(login, password)


    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_duplicate_courier(self):

        response, login, password, first_name = (register_new_courier_and_return_login_password())
        assert response.status_code == code_for_successful_courier_creation


        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        duplicate_response = duplicate_courier(payload)

        assert duplicate_response.status_code == duplicate_courier_creation_code
        assert duplicate_response.json() == the_body_of_the_duplicate_courier_creature

        courier_removal(login, password)


    @allure.title("Нельзя создать курьера без логина")
    def test_create_without_a_login(self):
        response, password, first_name = (registering_a_new_courier_without_a_login())

        assert response.status_code == courier_creation_code_without_a_required_field
        assert response.json() == courier_creation_body_without_a_required_field



    @allure.title("Нельзя создать курьера без пароля")
    def test_create_without_a_password(self):
        response, login, first_name = (registering_a_new_courier_without_a_password())

        assert response.status_code == courier_creation_code_without_a_required_field
        assert response.json() == courier_creation_body_without_a_required_field

