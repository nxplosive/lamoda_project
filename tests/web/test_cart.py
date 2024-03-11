import allure
import pytest

from lamoda_tests.data.data_cards import card
from lamoda_tests.pages.main_page import MainPage


@pytest.fixture()
def pre_add_to_cart():
    main_page = MainPage()
    main_page.open_url()
    main_page.search(card.card_name)
    main_page.add_item_to_cart(card.card_name)
    return main_page


@allure.epic('Add item to cart')
@allure.label("owner", "nsafonov")
@allure.feature("Checking whether an item has been added to cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_add_to_cart():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.card_name)
    main_page.add_item_to_cart(card.card_name)
    main_page.check_cart(card.card_name, card.brand_name, card.item_name)


@allure.epic('Remove item from cart')
@allure.label("owner", "nsafonov")
@allure.feature("Checking whether an item has been removed")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_remove_from_cart(pre_add_to_cart):
    main_page = pre_add_to_cart
    main_page.remove_from_cart()
