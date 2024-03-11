import json

import allure
import requests
from allure_commons._allure import step
from jsonschema import validate

from lamoda_tests.utils.schemas_path import load_schema


@allure.epic('API. Choose location')
@allure.label("owner", "nsafonov")
@allure.feature("Check of choosen location")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.label('layer', 'api')
@allure.severity('normal')
@allure.story('Выбор локации')
def test_location(base_url, header):
    with step("Выбор локации"):
        url = f"{base_url}/delivery/methods?city_aoid=7700000000000&ignore_cart=true"
    response = requests.request("GET", url, headers=header)
    body = response.json()
    with allure.step('Статус код = 200'):
        assert response.status_code == 200

    schema = load_schema("geo.json")
    with open(schema) as file:
        schema = json.load(file)
    validate(body, schema=schema)
