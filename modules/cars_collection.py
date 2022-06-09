from random import randint

from modules.car import Car


class CarsCollection:
    def __init__(self):
        self._cars: dict = self.generate_cars()

    def __str__(self):
        car_list: list = []

        for car in self._cars:
            car_list.append(str(self._cars[car]))

        return str(car_list)

    @property
    def cars(self):
        return self._cars

    @cars.setter
    def cars(self, value: dict):
        self._cars = value

    def generate_cars(self) -> dict:
        cars = {}
        for i in range(randint(3, 6)):
            cars[i] = Car()
        return cars

    def place_in_start_warehouses(self) -> None:
        for car_id in self._cars:
            self._cars[car_id].current_location_id = self._cars[car_id].start_warehouse
