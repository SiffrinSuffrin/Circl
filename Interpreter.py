import time, math
from Circl import *

def circlGen(program):
    subCircl = False
    tempchars = []
    toCircl = []

    for char in program:
        if char in ('"', "'"):
            if not subCircl:
                subCircl = True
            else:
                toCircl.append(Circl(tempchars))
                tempchars = []
                subCircl = False
            continue

        if subCircl:
            tempchars.append(char)
        else:
            toCircl.append(char)
    return toCircl

def decode():
    program = '"0"NP.'

    mainCircl = Circl(circlGen(program))
    print("Compiled a circl with radius ", mainCircl.radius())

    return mainCircl

def execute(mainCircl):
    programCounter = 0
    while True:

        if mainCircl.length() == 0:
            break

        instruction = mainCircl.access(programCounter)

        if type(instruction) is Circl:
            mainCircl.append(instruction)

        elif instruction == "˄":
            toPrint = mainCircl.pop()
            if type(toPrint) is Circl:
                print("".join(toPrint.wholeList()))
            else:
                print(toPrint)
        
        elif instruction == "˅":
            mainCircl.append(input())

        elif instruction == "!":
            toInvert = mainCircl.pop()
            if type(toInvert) is Circl:
                mainCircl.append(not(toInvert.wholeList()))
            else:
                mainCircl.append(not(toInvert))
        
        elif instruction == ".":
            break

        time.sleep(0.01)
        programCounter += 1

execute(decode())