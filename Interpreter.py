import time, sys

from Circl import Circl
from Program import Program
from InstructionSet import instruction_set

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
                    return Circl(to_circl), i + 1 # push multicircl
                else:
                    return "".join(str(item) for item in to_circl), i + 1 # push joined string
            else:
                sub_circl, skipable_letters = circl_gen(program[i + 1:], open_quotes + char)
                to_circl.append(sub_circl)
                last_substring_letter = i + skipable_letters
        else:
            to_circl.append(char) # append to main circl

    return Circl(to_circl), len(program)


def decode(program: str = ".") -> Circl:
    main_circl, _ = circl_gen(program)
    print("Compiled a circl with radius ", main_circl.radius())
    print(main_circl)
    return main_circl

def execute(main_circl):
    main_program = Program()

    while True:
        if len(main_circl) == 0:
            break
        try:
            command = main_circl.access(main_program.counter)
            instruction = instruction_set.get(command, None)
            if instruction:
                # instruction exists for command -> execute it
                instruction(main_circl, main_program)
            else:
                # unrecognized command -> append and continue
                main_circl.append(command)

        except Exception as e:
            print("An Exception, ", e, " occured. Pushing to stack and continuing")
            main_circl.append(str(e))

        # print(main_circl)
        main_program.counter += 1
        time.sleep(0.01)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        execute(decode(input()))
    else:
        execute(decode(input(sys.argv[1])))

# print(execute(decode('"hello world"^.'))) -> "hello world"
# print(execute(decode('12+^.'))) -> "3.0"