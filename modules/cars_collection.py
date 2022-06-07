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

    def generate_cars(self) -> dict:
        cars = {}
        for i in range(randint(3, 6)):
            cars[i] = Car()
        return cars
