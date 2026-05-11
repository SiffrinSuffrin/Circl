
import time
import traceback
from typing import cast
from typing import NamedTuple

from .circl import Circl
from .instruction_set import instruction_set, Instruction
from .program import main_program
from .source_info import SourcecodeInfo

class Program(NamedTuple):
    full_source: str
    offset: int

def decode(program: str = ".") -> Circl:
    main_circl = parse(program)
    # print(main_circl)
    print("Compiled a circl with radius ", main_circl.radius())
    return main_circl


def execute(executing_circl) -> Any | None:
    main_program.add_counter()
    while True:
        # print("-" * 2 * (main_program.number_of_counters()-1), executing_circl, f"counter is at {main_program.get_counter()}")
        if len(executing_circl) == 0:
            main_program.remove_counter()
            if main_program.number_of_counters() == 0:
                return executing_circl.stdout_copy
            break # Change this later to return the return-value instead
        current_step = main_program.get_counter()
        command = executing_circl[current_step]
        try:
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
            if isinstance(command, Circl) and command.source_info is not None:
                line_info: str
                if command.source_info.from_line == command.source_info.to_line:
                    line_info = f"line {command.source_info.from_line}"
                else:
                    line_info = f"lines {command.source_info.from_line} to {command.source_info.to_line}"

                position_info: str
                if command.source_info.from_position == command.source_info.to_position:
                    position_info = f"at position {command.source_info.from_position}"
                else:
                    position_info = f"from {command.source_info.from_position} to {command.source_info.to_position}"

                print(f"Exception in {command.source_info.file} on {line_info} {position_info}: {e}")
            else:
                print(f"Exception: {e}")
            if main_program.verbose_exceptions:
                traceback.print_stack()
            print("Appending current exception to current circl")
            executing_circl.append(str(e))

        main_program.increment_counter()
        time.sleep(0.01)
