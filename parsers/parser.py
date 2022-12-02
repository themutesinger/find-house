from abc import abstractclassmethod


class Parser:
    all_ads = []

    def __init__(
        self,
        *,
        price_from: int = 0,
        price_to: int = 1000000000,
        city: bool = True,
        uchactok: bool = True,
        house: bool = True
    ):
        self.price_from = price_from
        self.price_to = price_to
        self.city = city
        self.uchactok = uchactok
        self.house = house

    @abstractclassmethod
    def get_all() -> list[tuple]:
        pass

    def save_all():
        pass
