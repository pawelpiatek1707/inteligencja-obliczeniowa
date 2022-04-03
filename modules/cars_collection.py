from random import randint

from car import Car


class CarsCollection:
    def __init__(self):
        self._cars: dict = self.generate_cars()

    def generate_cars(self) -> dict:
        cars = {}
        for i in range(randint(3, 6)):
            cars[i] = Car()
        return cars
