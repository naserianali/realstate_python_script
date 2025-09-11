from abc import abstractmethod, ABC

from BaseModel import BaseModel


class Estate(ABC):
    def __init__(self, user, area, room_count, built_year, region, address, *args, **kwargs):
        self.user = user
        self.area = area
        self.room_count = room_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)


class Apartment(Estate):
    def __init__(self, has_elevator, has_parking, floor, *args, **kwargs):
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        self.floor = floor
        super().__init__(*args, **kwargs)


class House(Estate):
    def __init__(self, has_yard, floor_count, *args, **kwargs):
        self.has_yard = has_yard
        self.floor_count = floor_count
        super().__init__(*args, **kwargs)


class Store(Estate):
    pass