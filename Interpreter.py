import time, random, sys
from Circl import *

def circl_gen(program: str, open_quotes="") -> tuple[Circl, int]:
    to_circl = []
    last_substring_letter = -1
    for i, char in enumerate(program):
        if i <= last_substring_letter:
            continue

        if char in ('"', "'", "`"):
            if open_quotes and open_quotes[-1] is char:
                # Check if to_circl has any Circl objects
                has_circl = any(type(item) is Circl for item in to_circl)
                if has_circl:
                    return Circl(to_circl), i + 1
                else:
                    return "".join(str(item) for item in to_circl), i + 1
            else:
                sub_circl, skipable_letters = circl_gen(program[i + 1:], open_quotes + char)
                to_circl.append(sub_circl)
                last_substring_letter = i + skipable_letters
        else:
            to_circl.append(char)

    return Circl(to_circl), len(program)


def decode(program: str = ".") -> Circl:
    main_circl, _ = circl_gen(program)
    print("Compiled a circl with radius ", main_circl.radius())
    print(main_circl)
    return main_circl


def execute(main_circl):
    program_counter = 0

    while True:
        if len(main_circl) == 0:
            break
        try:
            instruction = main_circl.access(program_counter)

            if instruction == ".":
                while len(main_circl) > 0:
                    main_circl.pop()

            elif instruction == "˅":
                main_circl.append(input())

            elif instruction == "π":
                main_circl.append(str(math.pi))

            elif instruction == "ε":
                main_circl.append(str(math.e))

            elif instruction == "∞":
                main_circl.append(str(math.inf))

            elif instruction == "⧺":
                to_operate1 = main_circl.pop()
                main_circl.append(to_operate1)
                main_circl.append(to_operate1)

            elif instruction == "↓":
                main_circl.pop()

            elif instruction == "↶":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                to_operate3 = main_circl.pop()
                main_circl.append(to_operate2)
                main_circl.append(to_operate1)
                main_circl.append(to_operate3)

            elif instruction == "↷":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                to_operate3 = main_circl.pop()
                main_circl.append(to_operate1)
                main_circl.append(to_operate3)
                main_circl.append(to_operate2)

            elif instruction == "⇄":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                main_circl.append(to_operate1)
                main_circl.append(to_operate2)

            elif instruction == "@":
                to_operate1 = main_circl.pop()
                main_circl.append(main_circl.access(-(int(float(to_operate1)) + 1)))

            elif instruction == "^":
                to_operate1 = main_circl.pop()
                print(to_operate1)

            elif instruction == "§":
                to_operate1 = main_circl.pop()
                print(to_operate1, end="")

            elif instruction == "←":
                filename = main_circl.pop()
                with open(filename, "r") as f:
                    main_circl.append(f.read())

            elif instruction == "→":
                filename = main_circl.pop()
                to_operate1 = main_circl.pop()
                with open(filename, "w") as f:
                    f.write(str(to_operate1))

            elif instruction == "⇀":
                to_operate1 = main_circl.pop()
                main_circl.append(str(len(to_operate1)))

            elif instruction == "⦰":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(str(to_operate1.radius()))
                else:
                    main_circl.append(str(len(to_operate1)/(2*math.pi)))

            elif instruction == "♯":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(float(i)) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(float(to_operate1)))

            elif instruction == "♭":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(int(float(i))) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(int(float(to_operate1))))

            elif instruction == "Φ":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                precision = int(float(to_operate2))
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([f"{float(i):.{precision}f}" for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(f"{float(to_operate1):.{precision}f}")

            elif instruction == "Ψ":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(ord(i)) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(ord(to_operate1)))

            elif instruction == "Ω":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(chr(int(float(i)))) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(chr(int(float(to_operate1)))))

            elif instruction == "⚂":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(random.choice(to_operate1.whole_list()))
                else:
                    if to_operate1 == "1":
                        main_circl.append(str(random.random()))
                    else:
                        main_circl.append(str(random.randint(0, int(float(to_operate1)))))

            elif instruction == "¬":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl(["1" if not float(i) else "0" for i in to_operate1.whole_list()]))
                else:
                    main_circl.append("1" if not float(to_operate1) else "0")

            elif instruction == "∧":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append(Circl([str("1" if float(a) and float(b) else "0") for a, b in
                                             zip(to_operate2.whole_list(), to_operate1.whole_list())]))
                elif type(to_operate1) is Circl:
                    main_circl.append(
                        Circl(["1" if float(to_operate2) and float(i) else "0" for i in to_operate1.whole_list()]))
                elif type(to_operate2) is Circl:
                    main_circl.append(
                        Circl(["1" if float(i) and float(to_operate1) else "0" for i in to_operate2.whole_list()]))
                else:
                    main_circl.append("1" if float(to_operate1) and float(to_operate2) else "0")

            elif instruction == "∨":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append(Circl([str("1" if float(a) or float(b) else "0") for a, b in
                                             zip(to_operate2.whole_list(), to_operate1.whole_list())]))
                elif type(to_operate1) is Circl:
                    main_circl.append(
                        Circl(["1" if float(to_operate2) or float(i) else "0" for i in to_operate1.whole_list()]))
                elif type(to_operate2) is Circl:
                    main_circl.append(
                        Circl(["1" if float(i) or float(to_operate1) else "0" for i in to_operate2.whole_list()]))
                else:
                    main_circl.append("1" if float(to_operate1) or float(to_operate2) else "0")

            elif instruction == "⊕":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append(Circl([str(int(float(a)) ^ int(float(b))) for a, b in
                                             zip(to_operate2.whole_list(), to_operate1.whole_list())]))
                elif type(to_operate1) is Circl:
                    main_circl.append(
                        Circl([str(int(float(to_operate2)) ^ int(float(i))) for i in to_operate1.whole_list()]))
                elif type(to_operate2) is Circl:
                    main_circl.append(
                        Circl([str(int(float(i)) ^ int(float(to_operate1))) for i in to_operate2.whole_list()]))
                else:
                    main_circl.append(str(int(float(to_operate1)) ^ int(float(to_operate2))))

            elif instruction == "⋘":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append(Circl([str(int(float(a)) << int(float(b))) for a, b in
                                             zip(to_operate2.whole_list(), to_operate1.whole_list())]))
                elif type(to_operate1) is Circl:
                    main_circl.append(
                        Circl([str(int(float(to_operate2)) << int(float(i))) for i in to_operate1.whole_list()]))
                elif type(to_operate2) is Circl:
                    main_circl.append(
                        Circl([str(int(float(i)) << int(float(to_operate1))) for i in to_operate2.whole_list()]))
                else:
                    main_circl.append(str(int(float(to_operate2)) << int(float(to_operate1))))

            elif instruction == "⋙":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append(Circl([str(int(float(a)) >> int(float(b))) for a, b in
                                             zip(to_operate2.whole_list(), to_operate1.whole_list())]))
                elif type(to_operate1) is Circl:
                    main_circl.append(
                        Circl([str(int(float(to_operate2)) >> int(float(i))) for i in to_operate1.whole_list()]))
                elif type(to_operate2) is Circl:
                    main_circl.append(
                        Circl([str(int(float(i)) >> int(float(to_operate1))) for i in to_operate2.whole_list()]))
                else:
                    main_circl.append(str(int(float(to_operate2)) >> int(float(to_operate1))))

            elif instruction == "=":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append("1" if to_operate1.whole_list() == to_operate2.whole_list() else "0")
                else:
                    main_circl.append("1" if to_operate1 == to_operate2 else "0")

            elif instruction == "≠":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append("0" if to_operate1.whole_list() == to_operate2.whole_list() else "1")
                else:
                    main_circl.append("0" if to_operate1 == to_operate2 else "1")

            elif instruction == "<": #TODO: circls?
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                main_circl.append("1" if float(to_operate2) < float(to_operate1) else "0")

            elif instruction == ">": #TODO: circls?
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                main_circl.append("1" if float(to_operate2) > float(to_operate1) else "0")

            elif instruction == "≤": #TODO: circls?
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                main_circl.append("1" if float(to_operate2) <= float(to_operate1) else "0")

            elif instruction == "≥": #TODO: circls?
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                main_circl.append("1" if float(to_operate2) >= float(to_operate1) else "0")

            elif instruction == "⁇":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if not float(to_operate1):
                    program_counter += int(float(to_operate2))

            elif instruction == "‽":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if float(to_operate1):
                    program_counter += int(float(to_operate2))

            elif instruction == "⇒":
                to_operate1 = main_circl.pop()
                program_counter += int(float(to_operate1))

            elif instruction == "⇐":
                to_operate1 = main_circl.pop()
                program_counter = int(float(to_operate1)) - 1

            elif instruction == "↺":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    execute(to_operate1)

            elif instruction == "⊲":
                n = int(float(main_circl.pop()))
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    items = to_operate1.whole_list()
                    n = n % len(items) if items else 0
                    main_circl.append(Circl(items[n:] + items[:n]))
                else:
                    n = n % len(to_operate1) if to_operate1 else 0
                    main_circl.append(to_operate1[n:] + to_operate1[:n])

            elif instruction == "⊳":
                n = int(float(main_circl.pop()))
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    items = to_operate1.whole_list()
                    n = n % len(items) if items else 0
                    main_circl.append(Circl(items[-n:] + items[:-n]) if n else Circl(items))
                else:
                    n = n % len(to_operate1) if to_operate1 else 0
                    main_circl.append((to_operate1[-n:] + to_operate1[:-n]) if n else to_operate1)

            elif instruction == "⊙":
                n = int(float(main_circl.pop()))
                length = len(main_circl)
                n = n % length if length else 0
                items = main_circl.whole_list()
                rotated = items[n:] + items[:n]
                while len(main_circl) > 0:
                    main_circl.pop()
                for item in rotated:
                    main_circl.append(item)
                program_counter = (program_counter - n) % length - 1

            elif instruction == "⡳":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    #TODO: add step argument
                    main_circl.append(Circl([str(x) for x in range(int(float(to_operate1.whole_list()[0])),
                                                                   int(float(to_operate1.whole_list()[1])))]))
                else:
                    main_circl.append(Circl([str(x) for x in range(int(float(to_operate1)))]))

            elif instruction == "⇡":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(
                        Circl(Circl(str(x) for x in range(int(float(i)))) for i in to_operate1.whole_list()))
                else:
                    main_circl.append(Circl(str(x) for x in range(int(float(to_operate1)))))

            elif instruction == "²":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(float(i) ** 2) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(float(to_operate1) ** 2))

            elif instruction == "√":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(float(i) ** 0.5) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(float(to_operate1) ** 0.5))

            elif instruction == "ⁿ":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append(Circl(
                        [str(float(a) ** float(b)) for a, b in zip(to_operate2.whole_list(), to_operate1.whole_list())]))
                elif type(to_operate1) is Circl:
                    main_circl.append(Circl([str(float(to_operate2) ** float(i)) for i in to_operate1.whole_list()]))
                elif type(to_operate2) is Circl:
                    main_circl.append(Circl([str(float(i) ** float(to_operate1)) for i in to_operate2.whole_list()]))
                else:
                    main_circl.append(str(float(to_operate2) ** float(to_operate1)))

            elif instruction == "⌊":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(math.floor(float(i))) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(math.floor(float(to_operate1))))

            elif instruction == "⌈":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(math.ceil(float(i))) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(math.ceil(float(to_operate1))))

            elif instruction == "○":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(round(float(i))) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(round(float(to_operate1))))

            elif instruction == "⌃": #TODO: make this max over both operators
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(max(to_operate1.whole_list(), key=lambda x: float(x)))
                elif type(to_operate2) is Circl:
                    main_circl.append(max(to_operate2.whole_list(), key=lambda x: float(x)))
                else:
                    main_circl.append(str(max(float(to_operate1), float(to_operate2))))

            elif instruction == "⌄": #TODO: make this min over both operators
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(min(to_operate1.whole_list(), key=lambda x: float(x)))
                elif type(to_operate2) is Circl:
                    main_circl.append(min(to_operate2.whole_list(), key=lambda x: float(x)))
                else:
                    main_circl.append(str(min(float(to_operate1), float(to_operate2))))

            elif instruction == "|":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(abs(float(i))) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(abs(float(to_operate1))))

            elif instruction == "ℓ":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(math.log(float(i))) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(math.log(float(to_operate1))))

            elif instruction == "ℒ":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(math.log10(float(i))) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(math.log10(float(to_operate1))))

            elif instruction == "∿":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(math.sin(float(i))) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(math.sin(float(to_operate1))))

            elif instruction == "⌒":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(math.cos(float(i))) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(math.cos(float(to_operate1))))

            elif instruction == "∡":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(math.tan(float(i))) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(math.tan(float(to_operate1))))

            elif instruction == "✄":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([Circl(list(i)) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(Circl(list(to_operate1)))

            elif instruction == "⊂":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                to_operate3 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl(to_operate1.whole_list()[int(float(to_operate3)):int(float(to_operate2))]))
                else:
                    main_circl.append(to_operate1[int(float(to_operate3)):int(float(to_operate2))])

            elif instruction == "↔":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                to_operate3 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([i.replace(to_operate3, to_operate2) if type(i) is str else i for i in
                                             to_operate1.whole_list()]))
                else:
                    main_circl.append(to_operate1.replace(to_operate3, to_operate2))

            elif instruction == "⬆":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([i.upper() for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(to_operate1.upper())

            elif instruction == "⬇":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([i.lower() for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(to_operate1.lower())

            elif instruction == "∑":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(str(sum(float(i) for i in to_operate1.whole_list())))
                else:
                    main_circl.append(to_operate1)

            elif instruction == "⊗":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    result = 1.0
                    for i in to_operate1.whole_list():
                        result *= float(i)
                    main_circl.append(str(result))
                else:
                    main_circl.append(to_operate1)

            elif instruction == "∈":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append("1" if to_operate2 in to_operate1.whole_list() else "0")
                else:
                    main_circl.append("1" if to_operate2 in to_operate1 else "0")

            elif instruction == "∉":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append("1" if to_operate2 not in to_operate1.whole_list() else "0")
                else:
                    main_circl.append("1" if to_operate2 not in to_operate1 else "0")

            elif instruction == "⍳":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(str(lst.index(to_operate2)) if to_operate2 in to_operate1.whole_list() else "-1")
                else:
                    main_circl.append(str(to_operate1.find(to_operate2)))

            elif instruction == "∩":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append(Circl([i for i in to_operate2.whole_list() if i in set(to_operate1.whole_list())]))
                elif type(to_operate1) is Circl:
                    main_circl.append("".join(i for i in to_operate2 if i in set(to_operate1.whole_list())))
                elif type(to_operate2) is Circl:
                    main_circl.append("".join(i for i in to_operate1 if i in set(to_operate2.whole_list())))
                else:
                    main_circl.append("".join(i for i in to_operate2 if i in to_operate1))

            elif instruction == "∪":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    seen = set()
                    result = []
                    for i in to_operate2.whole_list() + to_operate1.whole_list():
                        if i not in seen:
                            seen.add(i)
                            result.append(i)
                    main_circl.append(Circl(result))
                else:
                    seen = set()
                    result = []
                    for i in to_operate2 if type(to_operate2) is str else "".join(
                            to_operate2.whole_list()) + to_operate1 if type(to_operate1) is str else "".join(
                            to_operate1.whole_list()):
                        if i not in seen:
                            seen.add(i)
                            result.append(i)
                    main_circl.append("".join(result))

            elif instruction == "⊖":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append(
                        Circl([i for i in to_operate2.whole_list() if i not in set(to_operate1.whole_list())]))
                elif type(to_operate1) is Circl:
                    main_circl.append("".join(i for i in to_operate2 if i not in set(to_operate1.whole_list())))
                elif type(to_operate2) is Circl:
                    main_circl.append(Circl([i for x in to_operate2.whole_list() if i != to_operate1]))
                else:
                    main_circl.append("".join(i for i in to_operate2 if i not in to_operate1))

            elif instruction == "⊛":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append(
                        Circl([Circl([a, b]) for a, b in zip(to_operate2.whole_list(), to_operate1.whole_list())]))
                elif type(to_operate1) is Circl:
                    main_circl.append(
                        Circl([Circl([a, b]) for a, b in zip(list(to_operate2), to_operate1.whole_list())]))
                elif type(to_operate2) is Circl:
                    main_circl.append(
                        Circl([Circl([a, b]) for a, b in zip(to_operate2.whole_list(), list(to_operate1))]))
                else:
                    main_circl.append(Circl([Circl([a, b]) for a, b in zip(list(to_operate2), list(to_operate1))]))

            elif instruction == "Δ":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    items = to_operate1.whole_list()
                    main_circl.append(
                        Circl([str(float(items[i + 1]) - float(items[i])) for i in range(len(items) - 1)]))
                else:
                    main_circl.append(to_operate1)

            elif instruction == "⌀":
                main_circl.append(str(len(main_circl)))

            elif instruction == "κ":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl(sorted(to_operate1.whole_list(),
                                                   key=lambda x: float(x) if x.replace('.', '', 1).lstrip(
                                                       '-').isdigit() else x)))
                else:
                    main_circl.append("".join(sorted(to_operate1)))

            elif instruction == "ρ":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl(list(reversed(to_operate1.whole_list()))))
                else:
                    main_circl.append(to_operate1[::-1])

            elif instruction == "χ":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                to_operate3 = main_circl.pop()
                if type(to_operate1) is Circl:
                    to_operate1.set(int(float(to_operate2)), to_operate3)
                    main_circl.append(to_operate1)
                else:
                    lst = list(to_operate1)
                    lst[int(float(to_operate2))] = to_operate3
                    main_circl.append("".join(lst))

            elif instruction == "≡":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    if to_operate1.whole_list()[1:] == to_operate1.whole_list()[:-1]:
                        main_circl.append("1")
                    else:
                        main_circl.append("0")
                else:
                    if list(to_operate1)[1:] == list(to_operate1)[:-1]:
                        main_circl.append("1")
                    else:
                        main_circl.append("0")

            elif instruction == "‾":
                to_operate1 = main_circl.pop()
                main_circl.append(Circl(to_operate1))

            elif instruction == "_":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    for i in to_operate1.whole_list():
                        main_circl.append(i)

            elif instruction == "⋃":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl:
                    if type(to_operate2) is Circl:
                        new_elements = []
                        base_list = to_operate1.whole_list()
                        for separator in to_operate2.whole_list():
                            joined_str = separator.join(base_list)
                            new_elements.append(Circl(joined_str))

                        main_circl.append(Circl(new_elements))
                    else:
                        main_circl.append(to_operate2.join(to_operate1.whole_list()))
                else:
                    if type(to_operate2) is Circl:
                        main_circl.append(to_operate1.join(to_operate2.whole_list()))
                    else:
                        main_circl.append(to_operate2.join(list(to_operate1)))

            elif instruction == "✂":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        new = []
                        for elem in to_operate2.whole_list():
                            new.append(Circl(i.split(elem) for i in to_operate1.whole_list()))
                        main_circl.append(Circl(new))
                    else:
                        main_circl.append(Circl(i.split(to_operate2) for i in to_operate1.whole_list()))
                else:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        main_circl.append(Circl(i.split(to_operate1) for i in to_operate2.whole_list()))
                    else:
                        main_circl.append(Circl(to_operate1.split(to_operate2)))

            elif instruction == "+":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        new = []
                        for elem in to_operate1.whole_list():
                            new.append(Circl([str(float(i) + float(elem)) for i in to_operate2.whole_list()]))
                        main_circl.append(Circl(new))
                    else:
                        main_circl.append(Circl([str(float(to_operate2) + float(i)) for i in to_operate1.whole_list()]))
                else:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        main_circl.append(Circl([str(float(to_operate1) + float(i)) for i in to_operate2.whole_list()]))
                    else:
                        main_circl.append(str(float(to_operate1) + float(to_operate2)))

            elif instruction == "-":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        new = []
                        for elem in to_operate1.whole_list():
                            new.append(Circl([str(float(i) - float(elem)) for i in to_operate2.whole_list()]))
                        main_circl.append(Circl(new))
                    else:
                        main_circl.append(Circl([str(float(to_operate2) - float(i)) for i in to_operate1.whole_list()]))
                else:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        main_circl.append(Circl([str(float(to_operate1) - float(i)) for i in to_operate2.whole_list()]))
                    else:
                        main_circl.append(str(float(to_operate1) - float(to_operate2)))

            elif instruction == "×":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        new = []
                        for elem in to_operate1.whole_list():
                            new.append(Circl([str(float(i) * float(elem)) for i in to_operate2.whole_list()]))
                        main_circl.append(Circl(new))
                    else:
                        main_circl.append(Circl([str(float(to_operate2) * float(i)) for i in to_operate1.whole_list()]))
                else:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        main_circl.append(Circl([str(float(to_operate1) * float(i)) for i in to_operate2.whole_list()]))
                    else:
                        main_circl.append(str(float(to_operate1) * float(to_operate2)))

            elif instruction == "÷":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        new = []
                        for elem in to_operate1.whole_list():
                            new.append(Circl([str(float(i) / float(elem)) for i in to_operate2.whole_list()]))
                        main_circl.append(Circl(new))
                    else:
                        main_circl.append(Circl([str(float(to_operate2) / float(i)) for i in to_operate1.whole_list()]))
                else:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        main_circl.append(Circl([str(float(to_operate1) / float(i)) for i in to_operate2.whole_list()]))
                    else:
                        main_circl.append(str(float(to_operate1) / float(to_operate2)))

            elif instruction == "%":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        new = []
                        for elem in to_operate1.whole_list():
                            new.append(Circl([str(float(i) % float(elem)) for i in to_operate2.whole_list()]))
                        main_circl.append(Circl(new))
                    else:
                        main_circl.append(Circl([str(float(to_operate2) % float(i)) for i in to_operate1.whole_list()]))
                else:
                    to_operate2 = main_circl.pop()
                    if type(to_operate2) is Circl:
                        main_circl.append(Circl([str(float(to_operate1) % float(i)) for i in to_operate2.whole_list()]))
                    else:
                        main_circl.append(str(float(to_operate1) % float(to_operate2)))

            elif instruction == "⁻":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(Circl([str(-float(i)) for i in to_operate1.whole_list()]))
                else:
                    main_circl.append(str(-float(to_operate1)))

            elif instruction == "∥":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl and type(to_operate2) is Circl:
                    main_circl.append(Circl(to_operate2.whole_list() + to_operate1.whole_list()))
                elif type(to_operate1) is Circl:
                    main_circl.append(Circl([to_operate2] + to_operate1.whole_list()))
                elif type(to_operate2) is Circl:
                    main_circl.append(Circl(to_operate2.whole_list() + [to_operate1]))
                else:
                    main_circl.append(to_operate2 + to_operate1)

            elif instruction == "⊡":
                to_operate1 = int(float(main_circl.pop()))
                to_operate2 = main_circl.pop()
                main_circl.append(Circl([to_operate2] * to_operate1))

            elif instruction == "τ":
                to_operate1 = main_circl.pop()
                main_circl.append(to_operate1)
                main_circl.append("circl" if type(to_operate1) is Circl else "string")

            elif instruction == "⌂":
                to_operate1 = main_circl.pop()
                if type(to_operate1) is Circl:
                    seen = []
                    result = []
                    for i in to_operate1.whole_list():
                        if i not in seen:
                            seen.append(i)
                            result.append(i)
                    main_circl.append(Circl(result))
                else:
                    seen = []
                    result = []
                    for i in to_operate1:
                        if i not in seen:
                            seen.append(i)
                            result.append(i)
                    main_circl.append("".join(result))

            elif instruction == "⊤":
                to_operate1 = int(float(main_circl.pop()))
                items = []
                for i in range(to_operate1):
                    items.append(main_circl.pop())
                main_circl.append(Circl(list(reversed(items))))

            elif instruction == "⊞":
                main_circl.append(str(program_counter))

            elif instruction == "ν":
                to_operate1 = main_circl.pop()
                to_operate2 = main_circl.pop()
                if type(to_operate1) is Circl:
                    main_circl.append(str(to_operate1.whole_list().count(to_operate2)))
                else:
                    main_circl.append(str(to_operate1.count(to_operate2)))

            else:
                main_circl.append(instruction)


        except Exception as e:
            print("An Exception, ", e, " occured. Pushing to stack and continuing")
            main_circl.append(str(e))

        # print(main_circl)
        program_counter += 1
        time.sleep(0.01)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        execute(decode(input()))
    else:
        execute(decode(input(sys.argv[1])))
