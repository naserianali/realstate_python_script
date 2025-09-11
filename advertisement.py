from BaseModel import BaseModel
from Estate import Apartment, House, Store
from Deal import Sell, Rent


class ApartmentSell(BaseModel, Apartment, Sell):

    def show_banner(self):
        print(f"price: {self.price_per_meter} discountable: {self.discountable} convertable {self.convertable}")


class ApartmentRent(BaseModel, Apartment, Rent):
    pass


class HouseSell(BaseModel, House, Sell):
    def show_banner(self):
        print(f"price: {self.price_per_meter} discountable: {self.discountable} convertable {self.convertable}")


class HouseRent(BaseModel, House, Rent):
    pass


class StoreSell(BaseModel, Store, Sell):
    def show_banner(self):
        print(f"price: {self.price_per_meter} discountable: {self.discountable} convertable {self.convertable}")


class StoreRent(BaseModel, Store, Rent):
    pass
