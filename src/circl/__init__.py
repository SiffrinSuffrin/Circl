from sys import exit

from . import instruction_set
from . import circl
from . import interpreter
from . import program

def main():
    from argparse import ArgumentParser # only import if main is called
    parser = ArgumentParser(description="Circl is a simple golfing language about cyclic arrays")
    parser.add_argument("source", help="The source code to execute. If not given or -, will read from stdin", default="-", nargs="?")
    parser.add_argument("-v", "--verbose-exceptions", help="Print full stack traces for exceptions", action="store_true", default=False)
    parsed = parser.parse_args()
    program.main_program.verbose_exceptions = parsed.verbose_exceptions
    source_code: str
    if parsed.source == "-":
        source_code = input("Enter your circl code: ")
    else:
        try: 
            with open(parsed.source, "r") as f:
                source_code = f.read()
        except FileNotFoundError:
            print(f"File {parsed.source} not found. Exiting.")
            exit(1)
    interpreter.execute(interpreter.decode(source_code))

