import time

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

    def access(self, location):
        return self.data[location % len(self.data)]

    def wholeList(self):
        return self.data


def decode():
    program = '"Hello, World!"P.'
    subCircl = False
    temp_chars = []
    toCircl = []

    for char in program:
        if char in ('"', "'"):
            if not subCircl:
                subCircl = True
            else:
                toCircl.append(Circl(temp_chars))
                temp_chars = []
                subCircl = False
            continue

        if subCircl:
            temp_chars.append(char)
        else:
            toCircl.append(char)

    mainCircl = Circl(toCircl)

    return mainCircl


def execute(mainCircl):
    programCounter = 0
    while True:
        instruction = mainCircl.access(programCounter)

        if type(instruction) is Circl:
            mainCircl.append(instruction)

        elif instruction == "P":
            toPrint = mainCircl.access(-1)
            if type(toPrint) is Circl:
                print("".join(toPrint.wholeList()))
            else:
                print(toPrint)
            mainCircl.remove(-1)
        
        elif instruction == ".":
            break

        time.sleep(0.01)
        programCounter += 1


execute(decode())

print("Program execution completed")
