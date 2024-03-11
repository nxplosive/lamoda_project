import json

import allure
import requests
from jsonschema import validate

from lamoda_tests.utils.schemas_path import load_schema
from tests.api.conftest import user_email, user_password, invalid_password, header


@allure.epic('API. Authorized')
@allure.label("owner", "nsafonov")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.label('layer', 'api')
@allure.severity('normal')
@allure.story('Успешная авторизация')
def test_authorization_registered_user(base_url):
    with allure.step('Успешная авторизация'):
        url = f"{base_url}customer/get"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': 'lid=ZEACrWW0zUcyREf7JKByAgA=; _gcl_au=1.1.815567332.1709861502; is_synced=true; UserReferrer=https://www.lamoda.ru/; XCookieNotifyWasShown=true; tildauid=1709947004580.518427; gd_city=%D0%B3.%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; gd_aoid=7700000000000; lmda_adBlocker=0; lmda_site_version=24.03.06; srv_menu_gender=men; search_gender=; seenFirstCoupon=true; noPhone=true; sessionId=17101266539358881140; _sp_ses.d14a=*; tildasid=1710126747085.524912; previousUrl=lamoda.ru%2Flp%2Flamoda_club%2F; authType=email; sid=MGM2MjkxOTBhOTQwYTdjYWUwYjE0ZGFhMDk1ZTA0MTc=|1710125187|b29152aa017f5ea0ea167e2fb4aba83995513ed1; LMDA=aoid=7700000000000; _sp_id.d14a=d0225a71-4b04-4d1e-95df-7e15189cf8d8.1709861503.10.1710126989.1710124330.4ce15503-2d3b-4be5-8bec-a06dfce914e7.ff43d7be-da76-4f7e-b9ac-0d0f16cfb482.8b4c8952-0895-4e9f-b310-57d47fbf449a.1710126656032.7; lid=ZEADnGXrn0OPoB9qNsH/AgA=',
        'Referer': 'https://www.lamoda.ru/lp/lamoda_club/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-gpc': '1'
    }
    response = requests.request("GET", url, json={"login": user_email, "password": user_password}, headers=headers)
    body = response.json()

    with allure.step('Статус код = 200'):
        assert response.status_code == 200

    schema = load_schema('authorization.json')
    with open(schema) as file:
        schema = json.load(file)
    validate(body, schema=schema)


@allure.epic('API. Authorized')
@allure.label("owner", "nsafonov")
@allure.feature("Checking the authorization of the user")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.label('layer', 'api')
@allure.severity('normal')
@allure.story('Безуспешная авторизация')
def test_failed_authorization(base_url, header):
    with allure.step('Безуспешная авторизация'):
        url = f"{base_url}customer/auth"
    response = requests.request("POST", url, json={"login": user_email, "password": invalid_password}, headers=header)
    body = response.json()
    with allure.step('Статус код = 403'):
        assert response.status_code == 403

    schema = load_schema('failed_authorization.json')
    with open(schema) as file:
        schema = json.load(file)
    validate(body, schema=schema)
