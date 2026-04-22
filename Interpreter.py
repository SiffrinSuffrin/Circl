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
    program = '"Hello, World!"˄.'

    mainCircl = Circl(circlGen(program))
    print("Compiled a circl with radius ", mainCircl.radius())

    return mainCircl

def recurseCircl(circl):
    toPrint = []
    for i in circl.wholeList():
        if type(i) is Circl:
            toPrint += [recurseCircl(i)]
        else:
            toPrint.append(i)
    return toPrint

def execute(mainCircl):
    programCounter = 0
    while True:

        if mainCircl.length() == 0:
            break

        instruction = mainCircl.access(programCounter)

        if type(instruction) is Circl:
            mainCircl.append(instruction)

        elif instruction == "˄":
            toOperate = mainCircl.pop()
            if type(toOperate) is Circl:
                print("".join(toOperate.wholeList()))
            else:
                print(toOperate)
        
        elif instruction == "˅":
            mainCircl.append(input())

        elif instruction == "!":
            toOperate = mainCircl.pop()
            if type(toOperate) is Circl:
                mainCircl.append(not(toOperate.wholeList()))
            else:
                mainCircl.append(not(toOperate))

        elif instruction == "+":
            toOperate = mainCircl.pop()
            if type(toOperate) is Circl:
                toOperate2 = mainCircl.pop()
                if type(toOperate2) is Circl:
                    new = []
                    for elem in toOperate2.wholeList():
                        new.append(Circl([str(int(elem) + int(i)) for i in toOperate.wholeList()]))
                    mainCircl.append(Circl(new))
                else:
                    mainCircl.append(Circl([str(int(toOperate2) + int(i)) for i in toOperate.wholeList()]))
            else:
                toOperate2 = mainCircl.pop()
                if type(toOperate2) is Circl:
                    mainCircl.append(Circl([str(int(toOperate) + int(i)) for i in toOperate2.wholeList()]))
                else:
                    mainCircl.append(str(int(toOperate)+int(toOperate2)))
        
        elif instruction == "²":
            toOperate = mainCircl.pop()
            if type(toOperate) is Circl:
                mainCircl.append(Circl([str(int(i)**2) for i in toOperate.wholeList()]))
            else:
                mainCircl.append(str(int(toOperate)**2))
        
        elif instruction == "√":
            toOperate = mainCircl.pop()
            if type(toOperate) is Circl:
                mainCircl.append(Circl([str(int(i)**(1/2)) for i in toOperate.wholeList()]))
            else:
                mainCircl.append(str(int(toOperate)**(1/2)))
        
        elif instruction == ".":
            break
        
        
        print(recurseCircl(mainCircl))
        time.sleep(1)
        programCounter += 1

execute(decode())