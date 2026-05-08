from __future__ import annotations
import math

type Point = int | str # primitive types

class Circl(list['Circl|Point']):
    def __repr__(self) -> str:
        as_list = super().__repr__()
        return 'Ͼ ' + as_list[1:-1] + ' Ͽ'

    def __str__(self) -> str:
        return self.__repr__()

    def __add__(self, other) -> Circl:
        match other:
            case Circl(other):
                pass
            case _:
                pass
    
    def __radd__(self, other):
        return self + other

    def __getitem__(self, index: int) -> Circl | Point:
        return super().__getitem__(index % len(self))

    def pop(self, index: int=-1) -> Circl | Point:
        return super().pop(i % len(self))

    def insert(self, index: int, obj: Circl | Point) -> Circl | Point:
        return super().insert(index % len(self), obj)

    def radius(self) -> float:
        return len(self)/(2*math.pi)