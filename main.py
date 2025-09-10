from random import choice

from Estate import Apartment, House, Store
from Rejon import Rejon
from User import User
from advertisement import ApartmentSell

FIRST_NAME = ["Ali", "Akbar", "Kobra"]
LAST_NAME = ["Akbari", "Asghari", 'Amjadi']
PHONE = ["09100229171", '09100229172', '09100229173', '09100229174', '09100229175']
if __name__ == '__main__':
    for phone in PHONE:
        User(choice(FIRST_NAME), choice(LAST_NAME), phone)

    for user in User.object_list:
        print(f"id: {user.id} : full name : {user.full_name}")

    r1 = Rejon("Tehran")
    print(r1.id)
    apt = Apartment(user=User.object_list[0], area=80, room_count=2, built_year=2020,
                    region=r1, address="Street 1", has_elevator=True,
                    has_parking=False, floor=3)

    house = House(user=User.object_list[2], area=120, room_count=3, built_year=2018,
                  region=r1, address="Street 2", has_yard=True,
                  floor_count=2)

    store = Store(user=User.object_list[1], area=40, room_count=1, built_year=2015,
                  region=r1, address="Street 3")

    apt.show_description()
    house.show_description()
    store.show_description()
    print(store.user.full_name)

    apartment_sell = ApartmentSell(
        user=User.object_list[0], area=80, room_count=2, built_year=2020,
        region=r1, address="Street 1", has_elevator=True,
        has_parking=False, floor=3, price_per_meter=100000,
        discountable=True, convertable=False
    )
    print(apartment_sell.show_banner())