import math
class Circl:
    def __init__(self, initial=[]):
        self.data = initial

    def extend(self, length):
        self.data += [""] * length

    def set(self, location, value):
        if isinstance(value, Circl):
            self.data[location % len(self.data)] = value
        else:
            self.data[location % len(self.data)] = str(value)

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
        return math.sqrt(len(self.data)/math.pi)
    
    def wholeList(self):
        return self.data