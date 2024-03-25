import allure

from lamoda_tests.data.data_cards import card
from lamoda_tests.pages.ui.main_page import MainPage


@allure.epic('Search item by name')
@allure.label("owner", "nsafonov")
@allure.feature("Checking item by name")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_search_by_name():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.card_name)
    main_page.result_by_name(card.card_name)


@allure.epic('Search item by brand')
@allure.label("owner", "nsafonov")
@allure.feature("Checking item by brand")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_search_by_brand():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.card_name)
    main_page.result_by_brand(card.brand_name)


@allure.epic('Search item by price')
@allure.label("owner", "nsafonov")
@allure.feature("Checking item by price")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_search_by_price():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.card_name)
    main_page.result_by_price(card.card_price)


@allure.epic('Search without result')
@allure.label("owner", "nsafonov")
@allure.feature("Checking unresulted operation")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_search_without_result():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.not_exist_data)
    main_page.no_result()
