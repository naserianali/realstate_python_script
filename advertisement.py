from Estate import Apartment, House, Store
from Deal import Sell, Rent


class ApartmentSell(Apartment, Sell):

    def show_banner(self):
        print(f"price: {self.price_per_meter} discountable: {self.discountable} convertable {self.convertable}")


class ApartmentRent(Apartment, Rent):
    pass


class HouseSell(House, Sell):
    def show_banner(self):
        print(f"price: {self.price_per_meter} discountable: {self.discountable} convertable {self.convertable}")


class HouseRent(House, Rent):
    pass


class StoreSell(Store, Sell):
    def show_banner(self):
        print(f"price: {self.price_per_meter} discountable: {self.discountable} convertable {self.convertable}")


class StoreRent(Store, Rent):
    pass
