import allure

from api.endpoints import *
from api.body_response import *
from conftest import *


class TestGetAListOfOrders:

    @allure.title("Список заказов")
    def test_get_a_list_of_orders(self):
        response_json = get_a_list_of_orders()

        assert orders_key_orders in response_json
        assert orders_key_pageInfo in response_json
        assert orders_key_availableStations in response_json

        assert isinstance(response_json[orders_key_orders], list)
        assert len(response_json[orders_key_orders]) > 0

        assert isinstance(response_json[orders_key_pageInfo], dict)
        assert len(response_json[orders_key_pageInfo]) > 0

        assert isinstance(response_json[orders_key_availableStations], list)
        assert len(response_json[orders_key_availableStations]) > 0
    
    