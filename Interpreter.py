import time, math
from Circl import *

def circlGen(program):
    subString = False
    tempchars = ""
    toCircl = []

    for char in program:
        if char in ('"', "'", "`"):
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
    program = '"REST"✄"TEST"✄⋃^.'
    mainCircl = Circl(circlGen(program))
    print("Compiled a circl with radius ", mainCircl.radius())

    return mainCircl

def recurseCircl(circl):
    if type(circl) == str:
        return circl
    items = circl.wholeList()
    toPrint = []
    for i in items:
        toPrint.append(recurseCircl(i))
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
                    print(recurseCircl(toOperate1))
                else:
                    print(toOperate1)

            elif instruction == "!":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl(["1" if not(int(i)) else "0" for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append("1" if not(int(toOperate1)) else "0")
                    
            elif instruction == "⇡":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl(Circl(str(x) for x in range(int(i))) for i in toOperate1.wholeList()))
                else:
                    mainCircl.append(Circl(str(x) for x in range(int(toOperate1))))
            
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
                    mainCircl.append(Circl(list(toOperate1)))
            
            elif instruction == "≡":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    if toOperate1.wholeList()[1:] == toOperate1.wholeList()[:-1]:
                        mainCircl.append("1")
                    else:
                        mainCircl.append("0")
                else:
                    if list(toOperate1)[1:] == list(toOperate1)[:-1]:
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
                        
            elif instruction == "⋃":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    if type(toOperate2) is Circl:
                        new_elements = []
                        base_list = toOperate1.wholeList() 
                        for separator in toOperate2.wholeList():
                            joined_str = separator.join(base_list)
                            new_elements.append(Circl(joined_str)) 
                            
                        mainCircl.append(Circl(new_elements))
                    else:
                        mainCircl.append(toOperate2.join(toOperate1.wholeList()))
                else:
                    if type(toOperate2) is Circl:
                        mainCircl.append(toOperate1.join(toOperate2.wholeList())) 
                    else:
                        mainCircl.append(toOperate2.join(list(toOperate1)))
                        
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
                        for elem in toOperate1.wholeList():
                            new.append(Circl([str(int(i) + int(elem)) for i in toOperate2.wholeList()]))
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
                        for elem in toOperate1.wholeList():
                            new.append(Circl([str(int(i) - int(elem)) for i in toOperate2.wholeList()]))
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
                        for elem in toOperate1.wholeList():
                            new.append(Circl([str(int(i) * int(elem)) for i in toOperate2.wholeList()]))
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
                        for elem in toOperate1.wholeList():
                            new.append(Circl([str(int(i) / int(elem)) for i in toOperate2.wholeList()]))
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
                        for elem in toOperate1.wholeList():
                            new.append(Circl([str(int(i) % int(elem)) for i in toOperate2.wholeList()]))
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
            print("An Exception, ",e," occured. Pushing to stack and continuing")
            mainCircl.append(str(e))

        print(recurseCircl(mainCircl))
        programCounter += 1
        time.sleep(0.01)

execute(decode())
