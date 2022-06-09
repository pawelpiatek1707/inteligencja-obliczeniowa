import random

from math import sqrt
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
        self._car_path: list[dict[str, int]] = []

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
    def plates_number(self):
        return self._plates_number

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

    def calculate_distance(self, point_a: dict[str, int], point_b: dict[str, int]) -> int:
        dist_x: int = abs(point_a["x"] - point_b["x"])
        dist_y: int = abs(point_a["y"] - point_b["y"])
        return int(sqrt(dist_x**2 + dist_y**2))

    def get_path(self) -> list[dict[str, int]]:
        return self._car_path

    def get_path_log(self) -> str:
        total_km: int = 0
        last_point = None

        for item in self._car_path:
            if last_point is None:
                last_point = item
                continue
            total_km += self.calculate_distance(last_point, item)
            last_point = item

        return f'[samochód-{self._plates_number}] pokonał trasę: ' + \
            '-'.join(str(item["id"]) for item in self._car_path) + \
            ' -> dystans: ' + str(total_km) + ' km'

    def add_path_log(self, point: dict[str, int], loaded: int, unloaded: int) -> None:
        if loaded > 0:
            self.add_load(loaded)
        if unloaded > 0:
            self.reduce_load(unloaded)

        item: dict = {
            "id": point["id"],
            "x": point["x"],
            "y": point["y"],
            "loaded": loaded,
            "unloaded": unloaded,
            "load": self._load,
            "capacity": self._max_capacity,
            "left_demand": point["products_to_receive"] if "products_to_receive" in point else 0,
            "left_supply": point["products_to_ship"] if "products_to_ship" in point else 0,
            "is_storage": point["storage"]
        }

        self._current_location_id = point["id"]
        self._car_path.append(item)
        print(f'[samochód-{self._plates_number}] udał się do punktu: ' + str(item))

    def add_load(self, load_to_add: int) -> None:
        load_after_add = self._load + load_to_add
        assert load_after_add <= self.max_capacity, \
            f'[samochód-{self._plates_number}] pojemność po załadowaniu {load_after_add} kg, ' + \
            f'a dopuszczalna {self.max_capacity} kg'
        self._load = load_after_add

    def reduce_load(self, load_to_reduce: int) -> None:
        load_after_reduce = self._load - load_to_reduce
        assert load_after_reduce >= 0, \
            f'[samochód-{self._plates_number}] pojemność po rozładowaniu {load_after_reduce} kg, ' + \
            f'więc rozładowano więcej niż było można'
        self._load = load_after_reduce
