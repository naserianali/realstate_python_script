from BaseModel import BaseModel
from Estate import Apartment, House, Store
from Deal import Sell, Rent


class ApartmentSell(BaseModel, Apartment, Sell):

    def show_banner(self):
        print(f"price: {self.price_per_meter} discountable: {self.discountable} convertable {self.convertable}")


class ApartmentRent(BaseModel, Apartment, Rent):
    def show_banner(self):
        print(
            f"initial_price= {self.initial_price} monthly_price= {self.monthly_price} discountable= {self.discountable} convertable= {self.convertable}")


class HouseSell(BaseModel, House, Sell):
    def show_banner(self):
        print(f"price: {self.price_per_meter} discountable: {self.discountable} convertable {self.convertable}")


class HouseRent(BaseModel, House, Rent):
    def show_banner(self):
        print(
            f"initial_price= {self.initial_price} monthly_price= {self.monthly_price} discountable= {self.discountable} convertable= {self.convertable}")


class StoreSell(BaseModel, Store, Sell):
    def show_banner(self):
        print(f"price: {self.price_per_meter} discountable: {self.discountable} convertable {self.convertable}")


class StoreRent(BaseModel, Store, Rent):
    def show_banner(self):
        print(
            f"initial_price= {self.initial_price} monthly_price= {self.monthly_price} discountable= {self.discountable} convertable= {self.convertable}")
