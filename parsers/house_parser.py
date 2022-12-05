from abc import abstractclassmethod


class HouseParser:

    all_ads = []

    def __init__(
        self,
        *,
        price_from: int = 1,
        price_to: int = 1000000000,
        city: bool = True,
        uchactok: bool = True,
        house: bool = True,
        area_from: int = 1,
        area_to: int = 1000000000

    ):
        self.price_from = price_from
        self.price_to = price_to
        self.city = city
        self.uchactok = uchactok
        self.house = house
        self.area_from = area_from
        self.area_to = area_to

    @abstractclassmethod
    def get_all() -> list[tuple]:
        pass

    def save_all():
        pass
