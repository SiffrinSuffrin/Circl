from __future__ import annotations
import math

type Point = int | float | bool | str # primitive types

class Circl(list['Circl|Point']):
    def __repr__(self) -> str:
        as_list = super().__repr__()
        return 'Ͼ ' + as_list[1:-1] + ' Ͽ'

    def __str__(self) -> str:
        return self.__repr__()

    def __add__(self, other: Circl | Point) -> Circl:
        match other:
            case Circl(other):
                return Circl([a + b for (a, b) in zip(self, other)])
            case _:
                return Circl([x + other for x in self])
    
    def __radd__(self, other: Circl | Point) -> Circl:
        return self + other

    def __iadd__(self, other: Circl | Point) -> Circl:
        self = self + other
        return self

    def __sub__(self, other: Circl | Point) -> Circl:
        match other:
            case Circl(other):
                return Circl([a - b for (a, b) in zip(self, other)])
            case _:
                return Circl([x - other for x in self])

    def __rsub__(self, other: Point) -> Circl:
        return Circl([x - other for x in self])

    def __isub__(self, other: Circl | Point) -> Circl:
        self = self - other
        return self

    def __mul__(self, other: Circl | Point) -> Circl:
        match other:
            case Circl(other):
                return Circl([a * b for (a, b) in zip(self, other)])
            case _:
                return Circl([x * other for x in self])
    
    def __rmul__(self, other: Point) -> Circl:
        return self * other

    def __imul__(self, other: Circl | Point) -> Circl:
        self = self * other
        return self

    def __truediv__(self, other: Circl | Point) -> Circl:
        match other:
            case Circl(other):
                return Circl([a / b for (a, b) in zip(self, other)])
            case _:
                return Circl([x / other for x in self])
    
    def __rtruediv__(self, other: Point) -> Circl:
        return Circl([other / x for x in self])

    def __itruediv__(self, other: Circl | Point) -> Circl:
        self = self / other
        return self

    def __floordiv__(self, other: Circl | Point) -> Circl:
        match other:
            case Circl(other):
                return Circl([a // b for (a, b) in zip(self, other)])
            case _:
                return Circl([x // other for x in self])
    
    def __floordiv__(self, other: Point) -> Circl:
        return Circl([other // x for x in self])

    def __ifloordiv__(self, other: Circl | Point) -> Circl:
        self = self // other
        return self

    def __pow__(self, other: Circl | Point) -> Circl:
        match other:
            case Circl(other):
                return Circl([a ** b for (a, b) in zip(self, other)])
            case _:
                return Circl([x ** other for x in self])

    def __rpow__(self, other: Point) -> Circl:
        return Circl([other ** x for x in self])

    def __ipow__(self, other: Circl | Point) -> Circl:
        self = self ** other
        return self

    def __neg__(self) -> Circl:
        return Circl([-x for x in self])

    def __abs__(self) -> Circl:
        return Circl([abs(x) for x in self])

    def __round__(self) -> Circl:
        return Circl([round(x) for x in self])

    def __floor__(self) -> Circl:
        return Circl([math.floor(x) for x in self])

    def __ceil__(self) -> Circl:
        return Circl([math.ceil(x) for x in self])

    def __getitem__(self, index: int) -> Circl | Point:
        return super().__getitem__(index % len(self))

    def pop(self, index: int=-1) -> Circl | Point:
        return super().pop(index % len(self))

    def insert(self, index: int, obj: Circl | Point) -> Circl | Point:
        return super().insert(index % len(self), obj)

    def radius(self) -> float:
        return len(self)/(2*math.pi)