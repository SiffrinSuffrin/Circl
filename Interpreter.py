import time, math, random
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
    program = '"a"Ψ⧺^Ω^.'
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
                mainCircl.append(str(math.pi))
                
            elif instruction == "⧺":
                toOperate1 = mainCircl.pop()
                mainCircl.append(toOperate1)
                mainCircl.append(toOperate1)

            elif instruction == "↓":
                mainCircl.pop()

            elif instruction == "~":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                toOperate3 = mainCircl.pop()
                mainCircl.append(toOperate2)
                mainCircl.append(toOperate1)
                mainCircl.append(toOperate3)

            elif instruction == "@":
                idx = mainCircl.pop()
                mainCircl.append(mainCircl.access(-(int(float(idx)) + 1)))

            elif instruction == "^":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    print(recurseCircl(toOperate1))
                else:
                    print(toOperate1)

            elif instruction == "§":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    print(recurseCircl(toOperate1), end="")
                else:
                    print(toOperate1, end="")

            elif instruction == "←":
                filename = mainCircl.pop()
                with open(filename, "r") as f:
                    mainCircl.append(f.read())

            elif instruction == "→":
                filename = mainCircl.pop()
                toOperate1 = mainCircl.pop()
                content = recurseCircl(toOperate1) if type(toOperate1) is Circl else toOperate1
                with open(filename, "w") as f:
                    f.write(str(content))
                    
            elif instruction == "⇀":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(str(toOperate1.length()))
                else:
                    mainCircl.append(str(len(toOperate1)))
            
            elif instruction == "⦰": 
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(str(toOperate1.radius()))
                else:
                    mainCircl.append(str((len(toOperate1) / math.pi) ** 0.5))

            elif instruction == "♯":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(float(i)) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(float(toOperate1)))

            elif instruction == "♭":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(int(float(i))) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(int(float(toOperate1))))

            elif instruction == "Φ":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                precision = int(float(toOperate2))
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([f"{float(i):.{precision}f}" for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(f"{float(toOperate1):.{precision}f}")
                    
            elif instruction == "Ψ":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(ord(i)) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(ord(toOperate1)))
            
            elif instruction == "Ω":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(chr(int(float(i)))) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(chr(int(float(toOperate1)))))
            
            elif instruction == "⚂":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(random.choice(toOperate1.wholeList()))
                else:
                    if toOperate1 == "1":
                        mainCircl.append(str(random.random()))
                    else:
                        mainCircl.append(str(random.randint(0, int(float(toOperate1)))))

            elif instruction == "!":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl(["1" if not float(i) else "0" for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append("1" if not float(toOperate1) else "0")

            elif instruction == "&":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl and type(toOperate2) is Circl:
                    mainCircl.append(Circl([str("1" if float(a) and float(b) else "0") for a, b in zip(toOperate2.wholeList(), toOperate1.wholeList())]))
                elif type(toOperate1) is Circl:
                    mainCircl.append(Circl(["1" if float(toOperate2) and float(i) else "0" for i in toOperate1.wholeList()]))
                elif type(toOperate2) is Circl:
                    mainCircl.append(Circl(["1" if float(i) and float(toOperate1) else "0" for i in toOperate2.wholeList()]))
                else:
                    mainCircl.append("1" if float(toOperate1) and float(toOperate2) else "0")

            elif instruction == "∨":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl and type(toOperate2) is Circl:
                    mainCircl.append(Circl([str("1" if float(a) or float(b) else "0") for a, b in zip(toOperate2.wholeList(), toOperate1.wholeList())]))
                elif type(toOperate1) is Circl:
                    mainCircl.append(Circl(["1" if float(toOperate2) or float(i) else "0" for i in toOperate1.wholeList()]))
                elif type(toOperate2) is Circl:
                    mainCircl.append(Circl(["1" if float(i) or float(toOperate1) else "0" for i in toOperate2.wholeList()]))
                else:
                    mainCircl.append("1" if float(toOperate1) or float(toOperate2) else "0")

            elif instruction == "⊕":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl and type(toOperate2) is Circl:
                    mainCircl.append(Circl([str(int(float(a)) ^ int(float(b))) for a, b in zip(toOperate2.wholeList(), toOperate1.wholeList())]))
                elif type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(int(float(toOperate2)) ^ int(float(i))) for i in toOperate1.wholeList()]))
                elif type(toOperate2) is Circl:
                    mainCircl.append(Circl([str(int(float(i)) ^ int(float(toOperate1))) for i in toOperate2.wholeList()]))
                else:
                    mainCircl.append(str(int(float(toOperate1)) ^ int(float(toOperate2))))

            elif instruction == "««":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl and type(toOperate2) is Circl:
                    mainCircl.append(Circl([str(int(float(a)) << int(float(b))) for a, b in zip(toOperate2.wholeList(), toOperate1.wholeList())]))
                elif type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(int(float(toOperate2)) << int(float(i))) for i in toOperate1.wholeList()]))
                elif type(toOperate2) is Circl:
                    mainCircl.append(Circl([str(int(float(i)) << int(float(toOperate1))) for i in toOperate2.wholeList()]))
                else:
                    mainCircl.append(str(int(float(toOperate2)) << int(float(toOperate1))))

            elif instruction == "»»":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl and type(toOperate2) is Circl:
                    mainCircl.append(Circl([str(int(float(a)) >> int(float(b))) for a, b in zip(toOperate2.wholeList(), toOperate1.wholeList())]))
                elif type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(int(float(toOperate2)) >> int(float(i))) for i in toOperate1.wholeList()]))
                elif type(toOperate2) is Circl:
                    mainCircl.append(Circl([str(int(float(i)) >> int(float(toOperate1))) for i in toOperate2.wholeList()]))
                else:
                    mainCircl.append(str(int(float(toOperate2)) >> int(float(toOperate1))))

            elif instruction == "=":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl and type(toOperate2) is Circl:
                    mainCircl.append("1" if toOperate1.wholeList() == toOperate2.wholeList() else "0")
                else:
                    mainCircl.append("1" if toOperate1 == toOperate2 else "0")

            elif instruction == "<":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                mainCircl.append("1" if float(toOperate2) < float(toOperate1) else "0")

            elif instruction == ">":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                mainCircl.append("1" if float(toOperate2) > float(toOperate1) else "0")

            elif instruction == "?":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if not float(toOperate1):
                    programCounter += int(float(toOperate2))

            elif instruction == "¿":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if float(toOperate1):
                    programCounter += int(float(toOperate2))

            elif instruction == "↺":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    execute(toOperate1)
                    
            elif instruction == "⇡":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl(Circl(str(x) for x in range(int(float(i)))) for i in toOperate1.wholeList()))
                else:
                    mainCircl.append(Circl(str(x) for x in range(int(float(toOperate1)))))
            
            elif instruction == "²":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(float(i) ** 2) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(float(toOperate1) ** 2))
        
            elif instruction == "√":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(float(i) ** 0.5) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(float(toOperate1) ** 0.5))

            elif instruction == "ⁿ":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl and type(toOperate2) is Circl:
                    mainCircl.append(Circl([str(float(a) ** float(b)) for a, b in zip(toOperate2.wholeList(), toOperate1.wholeList())]))
                elif type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(float(toOperate2) ** float(i)) for i in toOperate1.wholeList()]))
                elif type(toOperate2) is Circl:
                    mainCircl.append(Circl([str(float(i) ** float(toOperate1)) for i in toOperate2.wholeList()]))
                else:
                    mainCircl.append(str(float(toOperate2) ** float(toOperate1)))

            elif instruction == "⌊":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(math.floor(float(i))) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(math.floor(float(toOperate1))))

            elif instruction == "⌈":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(math.ceil(float(i))) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(math.ceil(float(toOperate1))))

            elif instruction == "○":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(round(float(i))) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(round(float(toOperate1))))

            elif instruction == "↑":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(max(toOperate1.wholeList(), key=lambda x: float(x)))
                elif type(toOperate2) is Circl:
                    mainCircl.append(max(toOperate2.wholeList(), key=lambda x: float(x)))
                else:
                    mainCircl.append(str(max(float(toOperate1), float(toOperate2))))

            elif instruction == "↧":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(min(toOperate1.wholeList(), key=lambda x: float(x)))
                elif type(toOperate2) is Circl:
                    mainCircl.append(min(toOperate2.wholeList(), key=lambda x: float(x)))
                else:
                    mainCircl.append(str(min(float(toOperate1), float(toOperate2))))

            elif instruction == "|":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([str(abs(float(i))) for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(str(abs(float(toOperate1))))
                    
            elif instruction == "✄":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl(list(i) for i in toOperate1.wholeList()))
                else:
                    mainCircl.append(Circl(list(toOperate1)))

            elif instruction == "«":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                toOperate3 = mainCircl.pop()
                start = int(float(toOperate3))
                end = int(float(toOperate2))
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl(toOperate1.wholeList()[start:end]))
                else:
                    mainCircl.append(toOperate1[start:end])

            elif instruction == "↔":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                toOperate3 = mainCircl.pop()
                needle = toOperate3
                replacement = toOperate2
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([i.replace(needle, replacement) if type(i) is str else i for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(toOperate1.replace(needle, replacement))

            elif instruction == "↑↑":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([i.upper() for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(toOperate1.upper())

            elif instruction == "↓↓":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl([i.lower() for i in toOperate1.wholeList()]))
                else:
                    mainCircl.append(toOperate1.lower())

            elif instruction == "∑":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(str(sum(float(i) for i in toOperate1.wholeList())))
                else:
                    mainCircl.append(toOperate1)

            elif instruction == "⊗":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    result = 1.0
                    for i in toOperate1.wholeList():
                        result *= float(i)
                    mainCircl.append(str(result))
                else:
                    mainCircl.append(toOperate1)

            elif instruction == "∈":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append("1" if toOperate2 in toOperate1.wholeList() else "0")
                else:
                    mainCircl.append("1" if toOperate2 in toOperate1 else "0")

            elif instruction == "∉":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append("1" if toOperate2 not in toOperate1.wholeList() else "0")
                else:
                    mainCircl.append("1" if toOperate2 not in toOperate1 else "0")

            elif instruction == "indexOf":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    lst = toOperate1.wholeList()
                    mainCircl.append(str(lst.index(toOperate2)) if toOperate2 in lst else "-1")
                else:
                    mainCircl.append(str(toOperate1.find(toOperate2)))

            elif instruction == "⌀":
                mainCircl.append(str(mainCircl.length()))

            elif instruction == "κ":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl(sorted(toOperate1.wholeList(), key=lambda x: float(x) if x.replace('.','',1).lstrip('-').isdigit() else x)))
                else:
                    mainCircl.append("".join(sorted(toOperate1)))

            elif instruction == "ρ":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    mainCircl.append(Circl(list(reversed(toOperate1.wholeList()))))
                else:
                    mainCircl.append(toOperate1[::-1])

            elif instruction == "χ":
                toOperate1 = mainCircl.pop()
                idx = mainCircl.pop()
                val = mainCircl.pop()
                if type(toOperate1) is Circl:
                    toOperate1.set(int(float(idx)), val)
                    mainCircl.append(toOperate1)
                else:
                    lst = list(toOperate1)
                    lst[int(float(idx))] = val
                    mainCircl.append("".join(lst))
            
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
                            new.append(Circl([str(float(i) + float(elem)) for i in toOperate2.wholeList()]))
                        mainCircl.append(Circl(new))
                    else:
                        mainCircl.append(Circl([str(float(toOperate2) + float(i)) for i in toOperate1.wholeList()]))
                else:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        mainCircl.append(Circl([str(float(toOperate1) + float(i)) for i in toOperate2.wholeList()]))
                    else:
                        mainCircl.append(str(float(toOperate1) + float(toOperate2)))

            elif instruction == "-":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        new = []
                        for elem in toOperate1.wholeList():
                            new.append(Circl([str(float(i) - float(elem)) for i in toOperate2.wholeList()]))
                        mainCircl.append(Circl(new))
                    else:
                        mainCircl.append(Circl([str(float(toOperate2) - float(i)) for i in toOperate1.wholeList()]))
                else:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        mainCircl.append(Circl([str(float(toOperate1) - float(i)) for i in toOperate2.wholeList()]))
                    else:
                        mainCircl.append(str(float(toOperate1) - float(toOperate2)))

            elif instruction == "×":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        new = []
                        for elem in toOperate1.wholeList():
                            new.append(Circl([str(float(i) * float(elem)) for i in toOperate2.wholeList()]))
                        mainCircl.append(Circl(new))
                    else:
                        mainCircl.append(Circl([str(float(toOperate2) * float(i)) for i in toOperate1.wholeList()]))
                else:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        mainCircl.append(Circl([str(float(toOperate1) * float(i)) for i in toOperate2.wholeList()]))
                    else:
                        mainCircl.append(str(float(toOperate1) * float(toOperate2)))
            
            elif instruction == "÷":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        new = []
                        for elem in toOperate1.wholeList():
                            new.append(Circl([str(float(i) / float(elem)) for i in toOperate2.wholeList()]))
                        mainCircl.append(Circl(new))
                    else:
                        mainCircl.append(Circl([str(float(toOperate2) / float(i)) for i in toOperate1.wholeList()]))
                else:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        mainCircl.append(Circl([str(float(toOperate1) / float(i)) for i in toOperate2.wholeList()]))
                    else:
                        mainCircl.append(str(float(toOperate1) / float(toOperate2)))

            elif instruction == "%":
                toOperate1 = mainCircl.pop()
                if type(toOperate1) is Circl:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        new = []
                        for elem in toOperate1.wholeList():
                            new.append(Circl([str(float(i) % float(elem)) for i in toOperate2.wholeList()]))
                        mainCircl.append(Circl(new))
                    else:
                        mainCircl.append(Circl([str(float(toOperate2) % float(i)) for i in toOperate1.wholeList()]))
                else:
                    toOperate2 = mainCircl.pop()
                    if type(toOperate2) is Circl:
                        mainCircl.append(Circl([str(float(toOperate1) % float(i)) for i in toOperate2.wholeList()]))
                    else:
                        mainCircl.append(str(float(toOperate1) % float(toOperate2)))
            
            elif instruction == "\\":
                toOperate1 = mainCircl.pop()
                toOperate2 = mainCircl.pop()
                toOperate3 = mainCircl.pop()
                mainCircl.append(toOperate3)
                mainCircl.append(toOperate1)
                mainCircl.append(toOperate2)
            
            else:
                mainCircl.append(instruction)
                

        except Exception as e:
            print("An Exception, ",e," occured. Pushing to stack and continuing")
            mainCircl.append(str(e))

        print(recurseCircl(mainCircl))
        programCounter += 1
        time.sleep(0.01)

execute(decode())
