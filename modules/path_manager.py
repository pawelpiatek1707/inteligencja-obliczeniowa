from math import sqrt


def calculate_distance(point_a: dict[str, int], point_b: dict[str, int]) -> int:
    dist_x: int = abs(point_a["x"] - point_b["x"])
    dist_y: int = abs(point_a["y"] - point_b["y"])
    return int(sqrt(dist_x**2 + dist_y**2))
