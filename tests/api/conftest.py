import pytest


@pytest.fixture
def base_url():
    base_url = "https://www.lamoda.ru/api/v1/"
    return base_url


@pytest.fixture
def header():
    headers = {
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 '
                      'Safari/537.3'
    }
    return headers
