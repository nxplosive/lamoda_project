import json

import allure
import requests
from allure_commons._allure import step


@allure.tag('api')
@allure.label('layer', 'API')
@allure.label('owner', 'nsafonov')
@allure.story('Удаление товара из корзины')
def test_cart_item(base_url):
    with step("Удаление товара из корзины"):
        url = f'{base_url}cart/remove'
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({
        "skus": [
            "RTLACZ076501NS00"
        ],
        "geo": {
            "city_aoid": "7700000000000"
        },
        "item_selection_enabled": True
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    with allure.step('Статус код = 200'):
        assert response.status_code == 200
    assert response.json()["total_quantity"] == 0
    assert response.json()["total_price"] == 0
