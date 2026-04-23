import time, math
from Circl import *

def circlGen(program):
    subString = False
    tempchars = ""
    toCircl = []

    for char in program:
        if char in ('"', "'"):
            if not subString:
                subString = True
            else:
                toCircl.append("".join(tempchars))
                tempchars = ""
                subString = False
            continue

        if subString:
            tempchars += char
        else:
            toCircl.append(char)
    return toCircl

def decode():
    program = '"split this string"✄^.'
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
        try:
            instruction = mainCircl.access(programCounter)
            
            if instruction == ".":
                while mainCircl.length() > 0:
                    mainCircl.pop()
        
            elif instruction == "˅":
                mainCircl.append(input())

            elif instruction == "π":
                mainCircl.append(math.pi)

            elif instruction == "^":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    print(",".join(toOperate1.wholeList()))
                else:
                    print(toOperate1)

            elif instruction == "!":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(not(toOperate1.wholeList()))
                else:
                    mainCircl.append(not(toOperate1))
            
            elif instruction == "²":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(int(i)**2) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(int(toOperate1)**2))
        
            elif instruction == "√":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(int(i)**(1/2)) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(int(toOperate1)**(1/2)))

            elif instruction == "|":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(abs(int(i))) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(abs(int(toOperate1))))
            
            elif instruction == "₁":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(1-int(i)) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(1-int(toOperate1)))
                    
            elif instruction == "✄":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl(list(i) for i in toOperate1.wholeList()))
                else:
                    mainCircl.append(list(toOperate1))
            
            elif instruction == "≡":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    if toOperate1.wholeList()[1:] == toOperate1.wholeList()[:-1]:
                        mainCircl.append("1")
                    else:
                        mainCircl.append("0")
                        
            elif instruction == "‾":
                toOperate1 = mainCircl.pop()
                mainCircl.append(Circl(toOperate1))
                
            elif instruction == "_":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    for i in toOperate1.wholeList():
                        mainCircl.append(i)
                        
            elif instruction == "/":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                mainCircl.append(toOperate1)
                mainCircl.append(toOperate2)
                
            elif instruction == "✂":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        new = []
                        for elem in toOperate2.wholeList():
                            new.append(Circl(i.split(elem) for i in toOperate1.wholeList()))
                        mainCircl.append(Circl(new))
                    else:
                        mainCircl.append(Circl(i.split(toOperate2) for i in toOperate1.wholeList()))
                else:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        mainCircl.append(Circl(i.split(toOperate1) for i in toOperate2.wholeList()))
                    else:
                        mainCircl.append(Circl(toOperate1.split(toOperate2)))
                
            elif instruction == "+":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        new = []
                        for elem in toOperate2.wholeList():
                            new.append(Circl([str(int(elem) + int(i)) for i in toOperate1.wholeList()]))
                        mainCircl.append(Circl(new))
                    else:
                        mainCircl.append(Circl([str(int(toOperate2) + int(i)) for i in toOperate1.wholeList()]))
                else:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        mainCircl.append(Circl([str(int(toOperate1) + int(i)) for i in toOperate2.wholeList()]))
                    else:
                        mainCircl.append(str(int(toOperate1) + int(toOperate2)))

            elif instruction == "-":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        new = []
                        for elem in toOperate2.wholeList():
                            new.append(Circl([str(int(elem) - int(i)) for i in toOperate1.wholeList()]))
                        mainCircl.append(Circl(new))
                    else:
                        mainCircl.append(Circl([str(int(toOperate2) - int(i)) for i in toOperate1.wholeList()]))
                else:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        mainCircl.append(Circl([str(int(toOperate1) - int(i)) for i in toOperate2.wholeList()]))
                    else:
                        mainCircl.append(str(int(toOperate1) - int(toOperate2)))

            elif instruction == "×":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        new = []
                        for elem in toOperate2.wholeList():
                            new.append(Circl([str(int(elem) * int(i)) for i in toOperate1.wholeList()]))
                        mainCircl.append(Circl(new))
                    else:
                        mainCircl.append(Circl([str(int(toOperate2) * int(i)) for i in toOperate1.wholeList()]))
                else:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        mainCircl.append(Circl([str(int(toOperate1) * int(i)) for i in toOperate2.wholeList()]))
                    else:
                        mainCircl.append(str(int(toOperate1) * int(toOperate2)))
            
            elif instruction == "÷":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        new = []
                        for elem in toOperate2.wholeList():
                            new.append(Circl([str(int(elem) / int(i)) for i in toOperate1.wholeList()]))
                        mainCircl.append(Circl(new))
                    else:
                        mainCircl.append(Circl([str(int(toOperate2) / int(i)) for i in toOperate1.wholeList()]))
                else:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        mainCircl.append(Circl([str(int(toOperate1) / int(i)) for i in toOperate2.wholeList()]))
                    else:
                        mainCircl.append(str(int(toOperate1) / int(toOperate2)))

            elif instruction == "%":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        new = []
                        for elem in toOperate2.wholeList():
                            new.append(Circl([str(int(elem) % int(i)) for i in toOperate1.wholeList()]))
                        mainCircl.append(Circl(new))
                    else:
                        mainCircl.append(Circl([str(int(toOperate2) % int(i)) for i in toOperate1.wholeList()]))
                else:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        mainCircl.append(Circl([str(int(toOperate1) % int(i)) for i in toOperate2.wholeList()]))
                    else:
                        mainCircl.append(str(int(toOperate1) % int(toOperate2)))
            
            else:
                mainCircl.append(instruction)

        except Exception as e:
            mainCircl.append(str(e))

        programCounter += 1
        print(recurseCircl(mainCircl))
        time.sleep(1)

execute(decode())
