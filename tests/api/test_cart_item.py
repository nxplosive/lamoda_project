import json

import allure
import requests
from allure_commons._allure import step
from jsonschema import validate

from lamoda_tests.utils.schemas_path import load_schema


@allure.epic('API. Add item to cart')
@allure.label("owner", "nsafonov")
@allure.feature("Checking add item to cart")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.label('layer', 'api')
@allure.severity('normal')
@allure.story('Добавление товара в корзину')
def test_cart_item(base_url):
    with step("Добавление товара в корзину"):
        url = f'{base_url}cart/add'
    price = 1899
    payload = json.dumps({
        "sku": "RTLACZ076501NS00",
        "geo": {
            "city_aoid": "7700000000000"
        },
        "item_selection_enabled": True
    })
    head = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': 'lid=ZEACrWW0zUcyREf7JKByAgA=; _gcl_au=1.1.815567332.1709861502; is_synced=true; UserReferrer=https://www.lamoda.ru/; XCookieNotifyWasShown=true; tildauid=1709947004580.518427; sessionId=17101112343936756481; gd_city=%D0%B3.%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; gd_aoid=7700000000000; _sp_ses.d14a=*; lmda_adBlocker=0; lmda_site_version=24.03.06; srv_menu_gender=men; sid=NzJiYWQ2MzMzNWQzMDQ0NjBlZjYzNjk5NDRlYzc4YzA=|1710110664|e1d1d6a6c592ba8e31d575e122a72c2f29a48143; LMDA=aoid=7700000000000; _sp_id.d14a=d0225a71-4b04-4d1e-95df-7e15189cf8d8.1709861503.7.1710112467.1709980269.2b23f940-7ed9-49ae-99ec-3c90ce01ced9.8db8dcb6-b37a-40fe-81ab-e830a6e45f52.23d3a7cc-f354-4eb6-8bb6-e428dde989ca.1710111236212.32; lid=ZEADnGXrn0OPoB9qNsH/AgA=',
        'Origin': 'https://www.lamoda.ru',
        'Referer': 'https://www.lamoda.ru/p/rtlacz076501/bags-adidas-ryukzak/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-gpc': '1'
    }
    response = requests.request("POST", url, headers=head, data=payload)
    body = response.json()
    with allure.step('Статус код = 200'):
        assert response.status_code == 200

    schema = load_schema('item_add.json')
    with open(schema) as file:
        schema = json.load(file)
    validate(body, schema=schema)

    assert response.json()["total_quantity"] == 1
    assert response.json()["total_price"] == price
