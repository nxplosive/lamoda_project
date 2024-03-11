import dataclasses


@dataclasses.dataclass
class Card:
    card_name: str
    brand_name: str
    card_price: str
    item_name: str
    not_exist_data: str


card = Card(
    card_name='Кроссовки GALAXY STAR M',
    brand_name='adidas',
    card_price='5 600 ₽',
    item_name='Кроссовки adidas\n38 RUS (6 UK)\nСерый',
not_exist_data = 'j23hfg554'
)

@dataclasses.dataclass
class Texts:
    nothing_found: str = 'Ничего не нашли по запросу'
    empty_cart: str = 'Корзина пока пустая'
