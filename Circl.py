import math

class Circl:
    def __init__(self, initial:list[str|Circl]|None=None):
        self.data:list[str|Circl] = initial if initial is not None else []

    def __len__(self) -> int:
        return len(self.data)

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
        return (len(self) / math.pi) ** 0.5

    def whole_list(self) -> list[str|Circl]:
        return self.data
