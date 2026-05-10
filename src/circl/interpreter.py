import sys
import time
import traceback

from .circl import Circl
from .instruction_set import instruction_set, Instruction
from .program import main_program


def circl_gen(program: str, open_quotes="") -> tuple[Circl, int]:
    to_circl = []
    last_substring_letter = -1
    for i, char in enumerate(program):
        if i <= last_substring_letter:
            continue
        # TODO: add {} and () and [] for subcircles
        # TODO: make the quotes " ' ` put in a single string instead of a subcircle
        # TODO: add \ for escaping characters
        #
        if char in ('"', "'", "`"):
            if open_quotes and open_quotes[-1] is char:
                return Circl(to_circl), i + 1  # push multicircl
            else:
                sub_circl, skipable_letters = circl_gen(
                    program[i + 1 :], open_quotes + char
                )
                to_circl.append(sub_circl)
                last_substring_letter = i + skipable_letters
        else:
            if char.isnumeric():
                char = int(char)
            to_circl.append(char)  # append to main circl

    return Circl(to_circl), len(program)


def decode(program: str = ".") -> Circl:
    main_circl, _ = circl_gen(program)
    # print(main_circl)
    print("Compiled a circl with radius ", main_circl.radius())
    return main_circl


def execute(executing_circl):
    main_program.add_counter()
    while True:
        # print("-" * 2 * (main_program.number_of_counters()-1), executing_circl, f"counter is at {main_program.get_counter()}")
        if len(executing_circl) == 0:
            main_program.remove_counter()
            break
        try:
            current_step = main_program.get_counter()
            command = executing_circl[current_step]

            if isinstance(command, Circl) or command not in instruction_set.keys():
                executing_circl.append(command)
            else:
                instruction: Instruction = instruction_set[command]

                # instruction exists for command -> execute it
                if instruction.calls_subroutine:
                    instruction.operation(executing_circl, execute)
                else:
                    instruction.operation(executing_circl)

        except Exception as e:
            traceback.print_exception(e)
            print("An Exception, ", e, " occured. Pushing to stack and continuing")
            executing_circl.append(str(e))

        main_program.increment_counter()
        time.sleep(0.01)
