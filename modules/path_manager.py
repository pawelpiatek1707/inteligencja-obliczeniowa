from math import sqrt

from modules.cars_collection import CarsCollection
from modules.car import Car


class PathManager:
    def __init__(self, warehouse_data: list[dict[str, int]], cars_data: CarsCollection) -> None:
        self._warehouse_data: list[dict[str, int]] = warehouse_data
        self._cars_data: CarsCollection = cars_data

    def calculate_distance(self, point_a: dict[str, int], point_b: dict[str, int]) -> int:
        dist_x: int = abs(point_a["x"] - point_b["x"])
        dist_y: int = abs(point_a["y"] - point_b["y"])
        return int(sqrt(dist_x**2 + dist_y**2))

    def place_cars_in_start_locations(self) -> None:
        for car_id in self._cars_data.cars:
            self._cars_data.cars[car_id].add_path_log(
                self._warehouse_data[self._cars_data.cars[car_id].current_location_id],
                self._cars_data.cars[car_id].max_capacity, 0
            )

    def check_if_all_warehouses_done(self) -> bool:
        for warehouse in self._warehouse_data:
            if warehouse["storage"]:
                continue
            if warehouse["products_to_receive"] > 0:
                return False
            if warehouse["products_to_ship"] > 0:
                return False
        return True

    def decision_making_rules(self, car: Car) -> dict[str, bool]:
        if car.max_capacity - car.load <= 200:
            return {
                "can_deliver": True,
                "can_recharge": False,
                "should_deliver": True,
                "should_recharge": False,
                "should_return": False
            }
        if 200 < car.max_capacity - car.load <= car.max_capacity * 0.5:
            return {
                "can_deliver": True,
                "can_recharge": True,
                "should_deliver": True,
                "should_recharge": False,
                "should_return": False
            }
        if car.max_capacity * 0.5 < car.max_capacity - car.load <= car.max_capacity - 400:
            return {
                "can_deliver": True,
                "can_recharge": True,
                "should_deliver": True,
                "should_recharge": True,
                "should_return": False
            }
        if car.max_capacity - 400 < car.max_capacity - car.load <= car.max_capacity - 200:
            return {
                "can_deliver": True,
                "can_recharge": True,
                "should_deliver": False,
                "should_recharge": True,
                "should_return": False
            }
        if True:
            return {
                "can_deliver": False,
                "can_recharge": True,
                "should_deliver": False,
                "should_recharge": True,
                "should_return": True
            }

    def solve_problem(self) -> None:
        self.place_cars_in_start_locations()

        while not self.check_if_all_warehouses_done():
            print('[trasa] istnieją jeszcze nieobsłużone magazyny, wyliczam dalej trasę pojazdów')

            for car in self._cars_data.cars:
                decision: dict[str, bool] = self.decision_making_rules(self._cars_data.cars[car])
                print(f"[samochód-{self._cars_data.cars[car].plates_number}] podejmuje decyzję: " + str(decision))
