from __future__ import annotations

import math

class Circl:
    def __init__(self, initial:list[str|Circl]|None=None):

        self.data:list[str|Circl] = initial if initial is not None else []

    def __len__(self) -> int:
        return len(self.data)

    def __str__(self) -> str:
        string = ",".join([repr(a) if isinstance(a,Circl) else str(a) for a in self.data])
        return string

    def __repr__(self) -> str:
        return f"({self})"

    def __eq__(self, value):
        if not isinstance(value, Circl):
            return False
        if len(self) != len(value):
            return False
        return all([a == b for a, b in zip(self.data, value.whole_list())])

    def __ne__(self, value):
        return not self == value

    def __lt__(self, value):
        if not isinstance(value, Circl):
            return all([a < value for a in self.data])
        return all([a < b for a, b in zip(self.data, value.whole_list())])

    def __le__(self, value):
        if not isinstance(value, Circl):
            return all([a <= value for a in self.data])
        return all([a <= b for a, b in zip(self.data, value.whole_list())])

    def __gt__(self, value):
        if not isinstance(value, Circl):
            return all([a > value for a in self.data])
        return all([a > b for a, b in zip(self.data, value.whole_list())])

    def __ge__(self, value):
        if not isinstance(value, Circl):
            return all([a >= value for a in self.data])
        return all([a >= b for a, b in zip(self.data, value.whole_list())])

    def __add__(self, value):
        if not isinstance(value, Circl):
            return Circl(list(map(lambda x: str(float(x)+float(value)), self.data)))
        else:
            return Circl([str(a+b) for a, b in zip(self.data, value.whole_list())])

    def __radd__(self, value):
        return self+value

    def __iadd__(self, value):
        self.data = self+value
        return self

    def __sub__(self, value):
        if not isinstance(value, Circl):
            return Circl(list(map(lambda x: str(float(x)-float(value)), self.data)))
        else:
            return Circl([str(float(a)-float(b)) for a, b in zip(self.data, value.whole_list())])

    def __rsub__(self, value):
        if not isinstance(value, Circl):
            return Circl(list(map(lambda x: str(float(value)-float(x)), self.data)))
        else:
            return Circl([str(float(b)-float(a)) for a, b in zip(self.data, value.whole_list())])

    def __isub__(self, value):
        self.data = self-value
        return self

    def __mul__(self, value):
        if not isinstance(value, Circl):
            return Circl(list(map(lambda x: str(float(x)*float(value)), self.data)))
        else:
            return Circl([str(a*b) for a, b in zip(self.data, value.whole_list())])

    def __rmul__(self, value):
        return self*value

    def __imul__(self, value):
        self.data = self*value
        return self

    def __truediv__(self, value):
        if not isinstance(value, Circl):
            return Circl(list(map(lambda x: str(float(x)/float(value)), self.data)))
        else:
            return Circl([str(float(a)/float(b)) for a, b in zip(self.data, value.whole_list())])

    def __rtruediv__(self, value):
        if not isinstance(value, Circl):
            return Circl(list(map(lambda x: str(float(value)/float(x)), self.data)))
        else:
            return Circl([str(float(b)/float(a)) for a, b in zip(self.data, value.whole_list())])

    def __itruediv__(self, value):
        self.data = self/value
        return self

    def __floordiv__(self, value):
        if not isinstance(value, Circl):
            return Circl(list(map(lambda x: str(float(x)//float(value)), self.data)))
        else:
            return Circl([str(float(a)//float(b)) for a, b in zip(self.data, value.whole_list())])

    def __rfloordiv__(self, value):
        if not isinstance(value, Circl):
            return Circl(list(map(lambda x: str(float(value)//float(x)), self.data)))
        else:
            return Circl([str(float(b)//float(a)) for a, b in zip(self.data, value.whole_list())])

    def __ifloordiv__(self, value):
        self.data = self//value
        return self

    def __pow__(self, value):
        if not isinstance(value, Circl):
            return Circl(list(map(lambda x: str(float(x)**float(value)), self.data)))
        else:
            return Circl([str(float(a)**float(b)) for a, b in zip(self.data, value.whole_list())])

    def __rpow__(self, value):
        if not isinstance(value, Circl):
            return Circl(list(map(lambda x: str(float(value)**float(x)), self.data)))
        else:
            return Circl([str(float(b)**float(a)) for a, b in zip(self.data, value.whole_list())])

    def __ipow__(self, value):
        self.data = self**value
        return self

    def __neg__(self):
        return Circl(list(map(lambda x: str(-float(x)), self.data)))

    def __abs__(self):
        return Circl(list(map(lambda x: str(abs(x)), self.data)))

    def __round__(self, value):
        return Circl(list(map(lambda x: str(round(float(x))), self.data)))
    def __floor__(self):
        return Circl(list(map(lambda x: str(math.floor(float(x))), self.data)))
    def __ceil__(self):
        return Circl(list(map(lambda x: str(math.ceil(float(x))), self.data)))

    def extend(self, values:list[str|Circl]) -> None:
        self.data.extend(values)

    def set(self, location:int, value:str|Circl) -> None:
        self.data[location % len(self)] = value if isinstance(value, Circl) else str(value)

    def append(self, value:str|Circl) -> None:
        self.data.append(value)

    def remove(self, location:int):
        del self.data[location % len(self)]

    def pop(self) -> str|Circl:
        return self.data.pop()

    def access(self, location:int) -> str|Circl:
        return self.data[location % len(self)]

    def radius(self) -> float:
        return len(self)/(2*math.pi)

    def whole_list(self) -> list[str|Circl]:
        return self.data
