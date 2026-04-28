import math

class Circl:
    def __init__(self, initial=None):
        self.data = initial if initial is not None else []

    def extend(self, length):
        self.data.extend([""] * length)

    def set(self, location, value):
        self.data[location % len(self.data)] = value if isinstance(value, Circl) else str(value)

    def append(self, value):
        self.extend(1)
        self.set(-1, value)

    def remove(self, location):
        del self.data[location]

    def pop(self):
        return self.data.pop()

    def access(self, location):
        return self.data[location % len(self.data)]

    def length(self):
        return len(self.data)

    def radius(self):
        return (len(self.data) / math.pi) ** 0.5

    def wholeList(self):
        return self.data
