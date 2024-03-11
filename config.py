from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    window_width: str = '1920'
    window_height: str = '1080'
    base_url: str = 'https://www.lamoda.ru'
    remote: bool = True
    page_load_strategy: str = 'normal'
    selenoid_capabilities: dict = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
