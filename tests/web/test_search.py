from lamoda_tests.data.data_cards import card
from lamoda_tests.pages.main_page import MainPage
import pytest


def test_search_by_name():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.card_name)
    main_page.result_by_name(card.card_name)


def test_search_by_brand():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.card_name)
    main_page.result_by_brand(card.brand_name)


def test_search_by_price():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.card_name)
    main_page.result_by_price(card.card_price)


def test_search_without_result():
    main_page = MainPage()

    main_page.open_url()
    main_page.search(card.not_exist_data)
    main_page.no_result()
