from sys import exit
from argparse import ArgumentParser

from .instruction_set import *
from .circl import *
from .interpreter import *
from .program import *

def main():
    parser = ArgumentParser(description="Circl is a simple golfing language about cyclic arrays")
    parser.add_argument("source", help="The source code to execute. If not given or -, will read from stdin", default="-")
    parser.add_argument("-v", "--verbose-exceptions", help="Print full stack traces for exceptions", action="store_true", default=False)
    parsed = parser.parse_args()
    main_program.verbose_exceptions = parsed.verbose_exceptions
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
    execute(decode(source_code))

