from __future__ import annotations

import math
from collections.abc import Iterable

type Point = int | float | bool | str  # primitive types


class Circl(list["Circl|Point"]):
    def __init__(self, circls_or_points: list["Circl|Point"] | Point = None):
        if isinstance(circls_or_points, Point.__value__):
            super().__init__([circls_or_points])
        elif isinstance(circls_or_points, Iterable):
            super().__init__(circls_or_points)
        elif circls_or_points is None:
            super().__init__([])
        else:
            raise TypeError(f"Expected types list['Circl|Point'] got instead type {type(circls_or_points)}")

        # TODO: refactor stdout_copy such that circl doesnt store this information anymore. Maybe move to class Program?
        self.stdout_copy = ""

    def __repr__(self) -> str:
        as_list = super().__repr__()
        return "Ͼ " + as_list[1:-1] + " Ͽ"

    def __str__(self) -> str:
        return self.__repr__()

    def __getitem__(self, index: int) -> Circl | Point:
        return super().__getitem__(index % len(self))

    def pop(self, index: int = -1) -> Circl | Point:
        return super().pop(index % len(self))

    def insert(self, index: int, obj: Circl | Point) -> Circl | Point:
        return super().insert(index % len(self), obj)

    def radius(self) -> float:
        return len(self) / (2 * math.pi)
