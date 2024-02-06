from item import Car
from queue import InvQueue


class Dealership:

    def __init__(self):
        self._available_cars = InvQueue()
        self._sold_cars = []

    def add_car(self, make, model, year, color, img):
        car = Car(make, model, year, color, img)
        self._available_cars.add(car)

    def sell_car(self, name, age):
        car = self._available_cars.get()
        car.sell(name, age)
        self._sold_cars.append(car)
        return car.to_dict()

    def list_available_cars(self):
        cars = self._available_cars.list()
        return [car.to_dict() for car in cars]

    def list_sold_cars(self):
        return [car.to_dict() for car in self._sold_cars]

    def get_the_car_for_sale(self):
        if not self._available_cars.is_epmty():
            return self._available_cars.display_last().to_dict()
        return None

if __name__ == "__main__":
    pass

