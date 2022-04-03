class Car:
    def __init__(self):
        self._max_capacity: int = 1000
        self._load: int = self._max_capacity

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
        load_after_add = self.load + load_to_add
        assert load_after_add < self.max_capacity, \
            f'Load after add will be {load_after_add}, but max capacity is {self.max_capacity}'
        self.load = load_after_add

    def reduce_load(self, load_to_reduce: int) -> None:
        load_after_reduce = self.load + load_to_reduce
        assert load_after_reduce > 0, \
            f'Load after reduce will be {load_after_reduce} and it less than 0'
        self.load = load_after_reduce
