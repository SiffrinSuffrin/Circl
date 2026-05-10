from .instruction_set import *
from .circl import *
from .interpreter import *
from .program import *

def main():
    if len(sys.argv) == 1:
        print("Put in circle string:")
        execute(decode(input()))
    else:
        execute(decode(sys.argv[1]))