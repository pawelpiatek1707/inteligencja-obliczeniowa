from math import sqrt

from modules.cars_collection import CarsCollection


class PathManager:
    def __init__(self, warehouse_data: list[dict[str, int]], cars_data: CarsCollection) -> None:
        self._warehouse_data: list[dict[str, int]] = warehouse_data
        self._cars_data: CarsCollection = cars_data

    def calculate_distance(self, point_a: dict[str, int], point_b: dict[str, int]) -> int:
        dist_x: int = abs(point_a["x"] - point_b["x"])
        dist_y: int = abs(point_a["y"] - point_b["y"])
        return int(sqrt(dist_x**2 + dist_y**2))

    def solve_problem(self) -> None:
        for car_id in self._cars_data.cars:
            self._cars_data.cars[car_id].add_path_log(
                self._warehouse_data[self._cars_data.cars[car_id].current_location_id],
                self._cars_data.cars[car_id].max_capacity, 0
            )
