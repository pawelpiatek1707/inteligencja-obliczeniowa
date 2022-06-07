import random

from random import sample


class Car:
    def __init__(self):
        chars: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums: str = '0123456789'
        self._max_capacity: int = sample([1000, 1500, 2000], k=1)[0]
        self._load: int = 0
        self._plates_number: str = ''.join([random.choice(chars) for i in range(2)]+[random.choice(nums) for i in range(5)])
        self._start_warehouse: int = random.randint(0, 4)
        self._current_location_id: int = -1

    def __str__(self):
        color: str = "zielony"
        if self._max_capacity == 1500:
            color = "niebieski"
        if self._max_capacity == 2000:
            color = "czerwony"

        return "[samochód] rejestracja: " + self._plates_number + \
               ", kolor: " + color + \
               ", magazyn ID: " + str(self._start_warehouse) + \
               ", pojemność: " + str(self._max_capacity) + " kg" + \
               ", ładunek: " + str(self._load) + " kg" + \
               ", aktualnie w punkcie ID: " + str(self._current_location_id)

    @property
    def start_warehouse(self):
        return self._start_warehouse

    @property
    def current_location_id(self):
        return self._current_location_id

    @current_location_id.setter
    def current_location_id(self, value: int):
        self._current_location_id = value

    @property
    def max_capacity(self) -> int:
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, value: int) -> None:
        self._max_capacity = value

    @property
    def load(self) -> int:
        return self._load

    @load.setter
    def load(self, value: int) -> None:
        self._load = value

    def add_load(self, load_to_add: int) -> None:
        load_after_add = self._load + load_to_add
        assert load_after_add < self.max_capacity, \
            f'[samochód] pojemność po załadowaniu {load_after_add} kg, a dopuszczalna {self.max_capacity} kg'
        self._load = load_after_add

    def reduce_load(self, load_to_reduce: int) -> None:
        load_after_reduce = self._load + load_to_reduce
        assert load_after_reduce > 0, \
            f'[samochód] pojemność po rozładowaniu {load_after_reduce} kg, więc rozładowano więcej niż było można'
        self._load = load_after_reduce
