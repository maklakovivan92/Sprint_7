import allure
import pytest

from api.endpoints import *
from api.body_response import *
from data.order_payload import *
from conftest import *


class TestCreatingAnOrder:

    @allure.title("Создание заказа с разными значениями color")
    @pytest.mark.parametrize(
        "color_value",
        [
            ["BLACK"],              
            ["GREY"],               
            ["BLACK", "GREY"],      
            None,                  
        ],
        ids=["black", "grey", "black_grey", "no_color"]
    )
    
    def test_create_order_with_color_variants(self, color_value):
        payload = BASE_ORDER_PAYLOAD
        payload["color"] = color_value
        response = create_order_with_color_variants(payload)

        assert response.status_code == order_creation_code
        assert order_track_key in response.json()

