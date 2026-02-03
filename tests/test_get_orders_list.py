import allure
import requests

from api.endpoints import *
from api.body_response import *


class TestGetAListOfOrders:

    @allure.title("Список заказов")
    def test_get_a_list_of_orders(self):
        response = requests.get(GET_ORDERS_LIST)

        assert response.status_code == successful_get_orders_list_code
        assert orders_key_orders in response.json()
        assert orders_key_pageInfo in response.json()
        assert orders_key_availableStations in response.json()